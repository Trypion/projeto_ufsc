function enableEditing(nome, university, ranking) {
  document.getElementById(nome).disabled =
    !document.getElementById(nome).disabled;
  document.getElementById(university).disabled =
    !document.getElementById(university).disabled;
  document.getElementById(ranking).disabled =
    !document.getElementById(ranking).disabled;
}

async function create() {
  const user = localStorage.getItem("user_id")

  const form = document.querySelector(".create-form");  
  console.log(form.elements)
  const name = form.elements.name.value;
  
  const email = form.elements.email.value;
  const sex = form.elements.sex.value;
  const age = parseInt(form.elements.age.value);
  const university_id = form.elements.university.value;
  const profile_picture = form.elements.profile_picture.value;
  const university_register = form.elements.university_register.value;
  const course_id = form.elements.course.value;
  const ranking = parseInt(form.elements.ranking.value);  

  const response = await fetch(`http://localhost:5000/profile/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-On-Behalf-Of": user,
    },
    body: JSON.stringify({ name, email, sex, age, university_id, profile_picture, university_register, course_id, ranking }),
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
  const user = localStorage.getItem("user_id")

  const form = document.querySelector(".form" + id);

  const name = form.elements.name.value;
  const university_id = form.elements.university.value;
  const ranking = parseInt(form.elements.ranking.value);  

  const response = await fetch(`http://localhost:5000/course/${id}`, {
    method: "PUT",
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

async function destroy(id) {
  const user = localStorage.getItem("user_id")
  await fetch(`http://localhost:5000/course/${id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "X-On-Behalf-Of": user,
    },
  });

  location.reload();
}
