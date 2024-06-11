function cancelForm() {
  document.getElementById("contratoForm").reset();
}

document
  .getElementById("contratoForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    alert("Formulario creado con éxito!");
    // Aquí puedes agregar la lógica para manejar el envío del formulario
  });
