const about = document.querySelector("#about");
const contact = document.querySelector("#contact");
const aboutContent = document.querySelector("#about-content");
const contactContent = document.querySelector("#contact-content");

about.addEventListener("click", () => {
  const aboutBox = new WinBox({
    title: "About Me",
    // modal: true,
    width: window.innerWidth/2,
    height: window.innerHeight/2,
    top: 50,
    right: 50,
    bottom: 50,
    left: 50,
    mount: aboutContent,
    onfocus: function () {
      this.setBackground("var(--text-color)");
    },
    onblur: function () {
      this.setBackground("#777");
    },
  });
});

contact.addEventListener("click", () => {
  const contactBox = new WinBox({
    title: "Contact Me",
    width: window.innerWidth/2,
    height: window.innerHeight/2,
    top: 100,
    right: 50,
    bottom: 50,
    left: 150,
    mount: contactContent,
    onfocus: function () {
      this.setBackground("var(--text-color)");
    },
    onblur: function () {
      this.setBackground("#777");
    },
  });
});
