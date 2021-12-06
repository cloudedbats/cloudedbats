document.addEventListener('DOMContentLoaded', () => {

  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach( el => {
      el.addEventListener('click', () => {

        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');

      });
    });
  }

});

// const navbar_burger_id = document.getElementById("navbar_burger_id");

const div_introduction_id = document.getElementById("div_introduction_id");
const div_bat_detectors_id = document.getElementById("div_bat_detectors_id");
const div_post_processing_id = document.getElementById("div_post_processing_id");
const div_future_plans_id = document.getElementById("div_future_plans_id");
const div_for_developers_id = document.getElementById("div_for_developers_id");
const div_about_id = document.getElementById("div_about_id");

function hideDivision(div_id) {
  if (div_id != 'undefined') {
    div_id.style.visibility = "hidden";
    div_id.style.overflow = "hidden";
    div_id.style.height = "0";
    div_id.style.width = "0";
  }
};

function showDivision(div_id) {
  if (div_id != 'undefined') {
    div_id.style.visibility = null;
    div_id.style.overflow = null;
    div_id.style.height = null;
    div_id.style.width = null;
  }
};

function hideShowParts(tab_name) {
  // navbar_burger_id.setAttribute("aria-expanded", "false");

  div_introduction_id.classList.remove("is-active");
  div_bat_detectors_id.classList.remove("is-active");
  div_post_processing_id.classList.remove("is-active");
  div_future_plans_id.classList.remove("is-active");
  div_for_developers_id.classList.remove("is-active");
  div_about_id.classList.remove("is-active");
  hideDivision(div_introduction_id)
  hideDivision(div_bat_detectors_id)
  hideDivision(div_post_processing_id)
  hideDivision(div_future_plans_id)
  hideDivision(div_for_developers_id)
  hideDivision(div_about_id)

  if (tab_name == "introduction") {
    div_introduction_id.classList.add("is-active");
    showDivision(div_introduction_id)
  } else if (tab_name == "bat-detectors") {
    div_bat_detectors_id.classList.add("is-active");
    showDivision(div_bat_detectors_id)
  } else if (tab_name == "post-processing") {
    div_post_processing_id.classList.add("is-active");
    showDivision(div_post_processing_id)
  } else if (tab_name == "future-plans") {
    div_future_plans_id.classList.add("is-active");
    showDivision(div_future_plans_id)
  } else if (tab_name == "for-developers") {
    div_for_developers_id.classList.add("is-active");
    showDivision(div_for_developers_id)
  } else if (tab_name == "about") {
    div_about_id.classList.add("is-active");
    showDivision(div_about_id)
  };
};



// // mobile menu
// const burgerIcon = document.querySelector('#burger');
// const navbarMenu = document.querySelector('#nav-links');

// burgerIcon.addEventListener('click', () => {
//   navbarMenu.classList.toggle('is-active');
// });

// // tabs
// const tabs = document.querySelectorAll('.tabs li');
// const tabContentBoxes = document.querySelectorAll('#tab-content > div');

// tabs.forEach(tab => {
//   tab.addEventListener('click', () => {
//     tabs.forEach(item => item.classList.remove('is-active'));
//     tab.classList.add('is-active');

//     const target = tab.dataset.target;
//     // console.log(target);
//     tabContentBoxes.forEach(box => {
//       if (box.getAttribute('id') === target) {
//         box.classList.remove('is-hidden');
//       } else {
//         box.classList.add('is-hidden');
//       }
//     })
//   })
// })

// // modal
// const signupButton = document.querySelector('#signup');
// const modalBg = document.querySelector('.modal-background');
// const modal = document.querySelector('.modal');

// signupButton.addEventListener('click', () => {
//   modal.classList.add('is-active');
// })

// modalBg.addEventListener('click', () => {
//   modal.classList.remove('is-active');
// }) 
