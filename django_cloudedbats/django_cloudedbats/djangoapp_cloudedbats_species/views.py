
import urllib.parse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from  cloudedbats_core import redlist_species 

from djangoapp_cloudedbats_species import models

def list_species(request):
    """ """
    # URL parameters. Also used next time on html page.
    selected_country = request.GET.get('country', 'All').upper()
    selected_family = request.GET.get('family', 'All').title()
    selected_genus = request.GET.get('genus', 'All').title()
    selected_redlist_category = request.GET.get('redlist_category', 'All').upper()
    # Filters for SpeciesChiroptera table.
    db_filter_dict = {}
    if selected_family not in ['', 'All']:
        db_filter_dict['{0}__{1}'.format('family_name', 'iexact')] = urllib.parse.unquote_plus(selected_family)
    if selected_genus not in ['', 'All']:
        db_filter_dict['{0}__{1}'.format('genus_name', 'iexact')] = urllib.parse.unquote_plus(selected_genus)
    if selected_redlist_category not in ['', 'ALL']:
        db_filter_dict['{0}__{1}'.format('category_global', 'iexact')] = urllib.parse.unquote_plus(selected_redlist_category)
    # Get rows from SpeciesChiroptera.
    species_db = models.SpeciesChiroptera.objects.filter(**db_filter_dict).order_by('scientific_name').values()
    # Get rows from ChiropteraByCountry.
    species_by_country_db = []
    if selected_country and (selected_country not in ['', 'ALL']):
        species_by_country_db = models.ChiropteraByCountry.objects.all().filter(country_isocode = selected_country).values()
    # Merge tables.
    selected_species_db = []
    taxa_for_country_dict = {}
    for row in species_by_country_db:
        taxa_for_country_dict[row['taxonid']] = row['category_country'] # TODO: Not used. Global does not differ from country level.
    row_no = 1 # For row numbering in html table.
    #
#     family_set = set()
#     genus_set = set()
    for species in species_db:
        if (selected_country in ['', 'ALL']) or (species['taxonid'] in taxa_for_country_dict.keys()):
            species['category_country'] = taxa_for_country_dict.get(species['taxonid'], '-')
            species['row_no'] = row_no
            row_no += 1
            selected_species_db.append(species)
            #
#             family_set.add(species['family_name'].title())
#             genus_set.add(species['genus_name'].title())
    # For html select option lists.
    countries_db = models.Countries.objects.order_by('country_name').values()
    family_db = models.SpeciesChiroptera.objects.values_list('family_name').order_by('family_name').distinct()
    family_list = [item[0].title() for item in family_db]
    genus_db = models.SpeciesChiroptera.objects.values_list('genus_name').order_by('genus_name').distinct()
    genus_list = [item[0] for item in genus_db]
#     family_list = sorted(family_set)
#     genus_list = sorted(genus_set)
    redlist_db = models.SpeciesChiroptera.objects.values_list('category_global').order_by('category_global').distinct()
    redlist_list = [item[0] for item in redlist_db]
    #
    return render(request, "cloudedbats_species.html", {'countries': countries_db,
                                                        'family_names': family_list,
                                                        'genus_names': genus_list,
                                                        'redlist_categories': redlist_list,
                                                        'selected_family_name': selected_family,
                                                        'selected_genus_name': selected_genus,
                                                        'selected_redlist_category': selected_redlist_category,
                                                        'selected_country': selected_country,
                                                        'species_db': selected_species_db})

def download(request):
    """ """
    out_header = [
        'Row',
        'Family',
        'Genus',
        'Scientific name',
        'IUCN Red list',
        'IUCN link',
        'EOL link',
        ]
    #
    # URL parameters.
    selected_country = request.GET.get('country', 'All').upper()
    selected_family = request.GET.get('family', 'All').title()
    selected_genus = request.GET.get('genus', 'All').title()
    selected_redlist_category = request.GET.get('redlist_category', 'All').upper()
    # Filters for SpeciesChiroptera table.
    db_filter_dict = {}
    if selected_family not in ['', 'All']:
        db_filter_dict['{0}__{1}'.format('family_name', 'iexact')] = urllib.parse.unquote_plus(selected_family)
    if selected_genus not in ['', 'All']:
        db_filter_dict['{0}__{1}'.format('genus_name', 'iexact')] = urllib.parse.unquote_plus(selected_genus)
    if selected_redlist_category not in ['', 'ALL']:
        db_filter_dict['{0}__{1}'.format('category_global', 'iexact')] = urllib.parse.unquote_plus(selected_redlist_category)
    # Get rows from SpeciesChiroptera.
    species_db = models.SpeciesChiroptera.objects.filter(**db_filter_dict).order_by('scientific_name').values()
    # Get rows from ChiropteraByCountry.
    species_by_country_db = []
    if selected_country and (selected_country not in ['', 'ALL']):
        species_by_country_db = models.ChiropteraByCountry.objects.all().filter(country_isocode = selected_country).values()
    # Merge tables.
    out_rows = []
    taxa_for_country_dict = {}
    for row in species_by_country_db:
        taxa_for_country_dict[row['taxonid']] = row['category_country'] # TODO: Not used. Global does not differ from country level.
    row_no = 1 # For row numbering in html table.
    #
    for species in species_db:
        if (selected_country in ['', 'ALL']) or (species['taxonid'] in taxa_for_country_dict.keys()):
            out_row = [str(row_no)]
            row_no += 1
            out_row.append(species['family_name'].title())
            out_row.append(species['genus_name'])
            out_row.append(species['scientific_name'])
            out_row.append(species['category_global'])
            out_row.append('http://maps.iucnredlist.org/map.html?id=' + species['taxonid'])
            out_row.append('http://eol.org/search?q=' + species['scientific_name'])
            out_rows.append(out_row)
    #
    response = HttpResponse(content_type = 'text/plain; charset=cp1252')    
    response['Content-Disposition'] = 'attachment; filename=chiroptera_iucn_red_list.txt'    
    response.write('\t'.join(out_header) + '\r\n') # Tab separated.
    for row in out_rows:
        response.write('\t'.join(map(str, row)) + '\r\n') # Tab separated.        
    return response

def update_red_list(request):
    """ """


    # To avoid total update during development...
    return render(request, "cloudedbats_species.html", {})
    
    
    
    
    # Get all needed data from IUCN.
    iunc_red_list = redlist_species.IucnRedList(debug = True)
    iunc_red_list.get_all_from_iucn_redlist()
    chiroptera_dict = iunc_red_list.get_iucn_chiroptera_dict()
    country_dict = iunc_red_list.get_iucn_country_dict()
    by_country_list = iunc_red_list.get_iucn_chiroptera_by_country_list()
    # Delete db tables.
    models.SpeciesChiroptera.objects.all().delete()
    models.Countries.objects.all().delete()
    models.ChiropteraByCountry.objects.all().delete()
    #
    for species_dict in chiroptera_dict.values():
        
        taxonid = species_dict.get('taxonid', '') 
        order_name = species_dict.get('order_name', '') 
        family_name = species_dict.get('family_name', '') 
        genus_name = species_dict.get('genus_name', '')
        scientific_name = species_dict.get('scientific_name', '') 
        population = species_dict.get('population', '') 
        category_global = species_dict.get('category', '')
            
        if taxonid:
            species_db = models.SpeciesChiroptera(
                taxonid = taxonid, 
                order_name = order_name if order_name else '-', 
                family_name = family_name if family_name else '-', 
                genus_name = genus_name if genus_name else '-',
                scientific_name = scientific_name if scientific_name else '-', 
                population = population if population else '-', 
                category_global = category_global if category_global else '-', 
            )
            species_db.save()
    #
    for isocode in country_dict.keys():
        
        country_name = country_dict[isocode] 
            
        country_db = models.Countries(
            country_isocode = isocode, 
            country_name = country_name, 
        )
        country_db.save()
    #
    for (country_isocode, taxonid, scientific_name, category) in by_country_list:
        
        by_country_db = models.ChiropteraByCountry(
            country_isocode = country_isocode, 
            taxonid = taxonid, 
            category_country = category if category else '', 
        )
        by_country_db.save()
    
    #
    return render(request, "cloudedbats_species.html", {})

