const searchicon1 = document.querySelector("#searchicon1");
const srchicon1 = document.querySelector("#srchicon1");
const search1 = document.querySelector("#searchinput1");

searchicon1.addEventListener('click', function(){
    search1.style.display = 'flex';
    searchicon1.style.display = 'none';
});

const userIcon = document.getElementById("userlap");
const loginPopup = document.getElementById("login-popup");
const closeLoginBtn = document.getElementById("close-login");

userIcon.addEventListener("click", () => {
  loginPopup.classList.remove("hidden");
});

closeLoginBtn.addEventListener("click", () => {
  loginPopup.classList.add("hidden");
});
// const searchBtn = document.getElementById('searchBtn');
// const searchPopup = document.getElementById('searchPopup');
// const closeBtn = document.getElementById('closeBtn');

// searchBtn.addEventListener('click', function() {
//     searchPopup.style.display = 'block';
// });

// closeBtn.addEventListener('click', function() {
//     searchPopup.style.display = 'none';
// });
function scrollToReservation() {
  // Assuming there is a section with id="reservation-form" for the booking form
  document.getElementById('reservation-form').scrollIntoView({ behavior: 'smooth' });
}

