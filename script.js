const roles = [
    "Aspiring Full Stack Developer",
    "Python Learner",
    "Future Data Analyst"
];

let roleIndex = 0;
let charIndex = 0;
let isDeleting = false;

const typingElement = document.querySelector(".hero h2");

function typeEffect() {

    const currentRole = roles[roleIndex];

    if (isDeleting) {
        typingElement.textContent =
            currentRole.substring(0, charIndex - 1);

        charIndex--;
    } else {
        typingElement.textContent =
            currentRole.substring(0, charIndex + 1);

        charIndex++;
    }

    let speed = isDeleting ? 50 : 100;

    if (!isDeleting && charIndex === currentRole.length) {
        speed = 1500;
        isDeleting = true;
    }

    else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        roleIndex = (roleIndex + 1) % roles.length;
        speed = 500;
    }

    setTimeout(typeEffect, speed);
}

typeEffect();