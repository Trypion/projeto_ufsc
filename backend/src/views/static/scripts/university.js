function enableEditing(nome, uf) {
  document.getElementById(nome).disabled =
    !document.getElementById(nome).disabled;
  document.getElementById(uf).disabled = !document.getElementById(uf).disabled;
}

async function create(){
  const user = localStorage.getItem("user_id")

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
    body = await response.json()
    alert(
      `Algo deu errado - status: ${response.status}, msg: ${body.error}`
    );
  }

  location.reload();

}

async function save(id) {
  const user = localStorage.getItem("user_id")
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
    body = await response.json()
    alert(
      `Algo deu errado - status: ${response.status}, msg: ${body.error}`
    );
  }

  location.reload();
}

async function destroy(id) {
  const user = localStorage.getItem("user_id")
  await fetch(`http://localhost:5000/university/${id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "X-On-Behalf-Of": user
    }
  });

  location.reload();
}
