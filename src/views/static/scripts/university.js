function enableEditing(nome, uf) {
  document.getElementById(nome).disabled =
    !document.getElementById(nome).disabled;
  document.getElementById(uf).disabled = !document.getElementById(uf).disabled;
}

async function create(){
  user = "Israel";

  form = document.querySelector(".create-form");

  const name = form.elements.name.value;
  const uf = form.elements.uf.value;

  const response = await fetch(`http://localhost:5000/university/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name, uf, user }),
  });

  if (response.status != 200) {
    alert("Algo deu errado");
  }

  location.reload();

}

async function save(id) {
  // user = localStorage.getItem("user")
  form = document.querySelector(".form" + id);

  const name = form.elements.name.value;
  const uf = form.elements.uf.value;

  user = "Israel";

  const response = await fetch(`http://localhost:5000/university/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name, uf, user }),
  });

  if (response.status != 200) {    
    alert("Algo deu errado");
  }

  location.reload();
}

async function destroy(id) {
  const user = "Israel";
  await fetch(`http://localhost:5000/university/${id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ user }),
  });

  location.reload();
}
