/**
 * Script para el dropdown de la sección de categorías
 */



const items = document.querySelectorAll(".item");
const tagsInput = document.querySelector(".tags-input");
const btnText = document.getElementById("btn-text");
const dropdownMenu = document.getElementById('dropdownMenu');

dropdownMenu.addEventListener('click', function(event) {
  // Evita que el clic en los items se propague y cierre el dropdown
  event.stopPropagation();
});


items.forEach(item => {

  item.addEventListener("click", () => {

    item.classList.toggle("checked");

    let checked = document.querySelectorAll(".checked");

    checked = Array.from(checked);

    if (checked && checked.length > 0) {
      const tags= checked.map(checkedItem => checkedItem.innerText).join(", ");
      tagsInput.value = tags
      btnText.innerText = tags
    } else {
      tagsInput.value = "";
      btnText.innerText = "Selecciona los tags"
    }

  });

});