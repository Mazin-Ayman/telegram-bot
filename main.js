
new TypeIt('.job', {
    speed: 80,
    loop: true, 
    backSpeed: 70,
    loopDelay: 800,
    waitUntilVisible: true,
})
.type("Frontend developer")
.pause(2500)
.delete()
.type("Backend developer")
.pause(2500)
.go();

new TypeIt('#anim',{
    speed:  40,
    loop: true, 
    backSpeed: 30,
    loopDelay: 800,
    waitUntilVisible: true,
})
.type("I develop Html, css, js frontend apps")
.pause(2500)
.delete()
.type("I develop NodeJs backend apps")
.pause(2500)
.go();
new TypeIt('.logo', {
    speed: 200,
    waitUntilVisible: true,
    cursor: false
}).go();




const mainBtn = document.querySelector('.main-btn');
/*
mainBtn.addEventListener('click',()=>{
    mainBtn.style.animation = "none";
}) 
*/