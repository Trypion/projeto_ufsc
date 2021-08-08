function enableEditing(nome, university, ranking) {
  document.getElementById(nome).disabled =
    !document.getElementById(nome).disabled;
  document.getElementById(university).disabled =
    !document.getElementById(university).disabled;
  document.getElementById(ranking).disabled =
    !document.getElementById(ranking).disabled;
}

async function create() {
  const user = "05f92ee5-7bd5-449f-b07d-15705064e08f";

  form = document.querySelector(".create-form");

  const name = form.elements.name.value;
  const university_id = form.elements.university.value;
  const ranking = parseInt(form.elements.ranking.value);

  const response = await fetch(`http://localhost:5000/course/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-On-Behalf-Of": user,
    },
    body: JSON.stringify({ name, university_id, ranking }),
  });

 

  
  if (response.status != 200) {
    body = await response.json()
    alert(
      `Algo deu errado - status: ${response.status}, msg: ${body.error}`
    );
  }

  location.reload();
}

async function save(id) {
  // user = localStorage.getItem("user")
  form = document.querySelector(".form" + id);

  const name = form.elements.name.value;
  const university = form.elements.university.value;
  const ranking = form.elements.ranking.value;

  const user = "05f92ee5-7bd5-449f-b07d-15705064e08f";

  const response = await fetch(`http://localhost:5000/university/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-On-Behalf-Of": user,
    },
    body: JSON.stringify({ name, university, ranking }),
  });

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
      "X-On-Behalf-Of": user,
    },
  });

  location.reload();
}
