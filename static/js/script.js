document.getElementById('link-movies').addEventListener('click', function() {
    var carousel = new bootstrap.Carousel(document.querySelector('#carouselExampleIndicators'));
    carousel.to(0);
});

document.getElementById('link-characters').addEventListener('click', function() {
    var carousel = new bootstrap.Carousel(document.querySelector('#carouselExampleIndicators'));
    carousel.to(1);
});

document.getElementById('link-books').addEventListener('click', function() {
    var carousel = new bootstrap.Carousel(document.querySelector('#carouselExampleIndicators'));
    carousel.to(2);
});


function clip(){
    document.getElementById("card").classList.toggle("flipped");

}