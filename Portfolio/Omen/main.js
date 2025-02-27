document.addEventListener('DOMContentLoaded', () => {
    const item1 = document.getElementById('item1');
    const item2 = document.getElementById('item2');
    const item3 = document.getElementById('item3');
    const item4 = document.getElementById('item4');
    const slider = document.getElementById('slider');
    const modal1 = document.getElementById('modal1');
    const modal2 = document.getElementById('modal2');
    const modal3 = document.getElementById('modal3');
    const modal4 = document.getElementById('modal4');

    // Add event listeners
    item1.addEventListener('mouseover', function() {
        slider.style.animationPlayState = "paused";
        modal1.classList.add('open');
    });

    item1.addEventListener('mouseout', function() {
        slider.style.animationPlayState = "running";
        modal1.classList.remove('open');
    });

    item2.addEventListener('mouseover', function() {
        slider.style.animationPlayState = "paused";
        modal2.classList.add('open');
    });

    item2.addEventListener('mouseout', function() {
        slider.style.animationPlayState = "running";
        modal2.classList.remove('open');
    });

    item3.addEventListener('mouseover', function() {
        slider.style.animationPlayState = "paused";
        modal3.classList.add('open');
    });

    item3.addEventListener('mouseout', function() {
        slider.style.animationPlayState = "running";
        modal3.classList.remove('open');
    });

    item4.addEventListener('mouseover', function() {
        slider.style.animationPlayState = "paused";
        modal4.classList.add('open');
    });

    item4.addEventListener('mouseout', function() {
        slider.style.animationPlayState = "running";
        modal4.classList.remove('open');
    });
});