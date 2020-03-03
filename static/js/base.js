window.sr = ScrollReveal();
sr.reveal('.navbar',{
  duration: 2000,
  origin: 'bottom',
  reset: true,
});
sr.reveal('.header-content-left',{
  duration: 2000,
  origin: 'left',
  distance: '300px',
  reset: true,
});
sr.reveal('.header-content-right',{
  duration: 2000,
  origin: 'right',
  distance: '300px',
  reset: true,
});
sr.reveal('#testimonial',{
  duration: 2000,
  origin: 'right',
  distance: '300px',
  viewFactor: 0.5,
  reset: true,
});
sr.reveal('.about-right',{
  duration: 2000,
  origin: 'right',
  diley: 1000,
  reset: true,
});
sr.reveal('.about-left',{
  origin : 'left',
  delay    : 200,
  distance : '120px',
  easing   : 'ease-in-out',
  reset: true,
});
sr.reveal('.contact-left',{
  origin : 'top',
  delay    : 200,
  distance : '120px',
  easing   : 'ease-in-out',
  reset: true,
});
sr.reveal('.contact-right',{
  duration   : 2000,
  distance   : '200px',
  easing     : 'ease-out',
  origin     : 'bottom',
  reset: true,
});
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
