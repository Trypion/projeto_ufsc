function enableEditing(nome, uf) {
  document.getElementById(nome).disabled =
    !document.getElementById(nome).disabled;
  document.getElementById(uf).disabled = !document.getElementById(uf).disabled;
}

async function create(){
  const user = "05f92ee5-7bd5-449f-b07d-15705064e08f";

  const form = document.querySelector(".create-form");

  const name = form.elements.name.value;
  const uf = form.elements.uf.value;

  const response = await fetch(`http://localhost:5000/university/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-On-Behalf-Of": user
    },
    body: JSON.stringify({ name, uf }),
  }).catch(err => console.log(err));

  if (response.status != 200) {
    alert(`Algo deu errado - ${response.body}`);
  }

  location.reload();

}

async function save(id) {
  const user = "05f92ee5-7bd5-449f-b07d-15705064e08f";
  const form = document.querySelector(".form" + id);

  const name = form.elements.name.value;
  const uf = form.elements.uf.value;


  const response = await fetch(`http://localhost:5000/university/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-On-Behalf-Of": user
    },
    body: JSON.stringify({ name, uf }),
  }).catch(err => console.log(err));

  if (response.status != 200) {    
    alert(`Algo deu errado - ${response.body}`);
  }

  location.reload();
}

async function destroy(id) {
  const user = "05f92ee5-7bd5-449f-b07d-15705064e08f";
  await fetch(`http://localhost:5000/university/${id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "X-On-Behalf-Of": user
    }
  });

  location.reload();
}
