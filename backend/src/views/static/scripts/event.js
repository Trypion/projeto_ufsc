function enableEditing(
  nome,
  email,
  sex,
  age,
  university,
  profile_picture,
  university_register,
  course,
  ranking
) {
  document.getElementById(nome).disabled =
    !document.getElementById(nome).disabled;
  document.getElementById(university).disabled =
    !document.getElementById(university).disabled;
  document.getElementById(email).disabled =
    !document.getElementById(email).disabled;
  document.getElementById(sex).disabled =
    !document.getElementById(sex).disabled;
  document.getElementById(age).disabled =
    !document.getElementById(age).disabled;
  document.getElementById(profile_picture).disabled =
    !document.getElementById(profile_picture).disabled;
  document.getElementById(university_register).disabled =
    !document.getElementById(university_register).disabled;
  document.getElementById(course).disabled =
    !document.getElementById(course).disabled;
  document.getElementById(ranking).disabled =
    !document.getElementById(ranking).disabled;
}

async function create() {
  const user = localStorage.getItem("user_id");

  const form = document.querySelector(".create-form");

  const name = form.elements.name.value;
  const start_at = form.elements.start_at.value;
  const end_at = form.elements.end_at.value;
  const description = form.elements.description.value;
  const event_picture = form.elements.event_picture.value;
  const location_ = form.elements.location.value;
  const reward = parseInt(form.elements.reward.value);

  if (new Date(start_at) > new Date(end_at)){
    return alert(`A data inicial tem que ser maior que a final`);
  }

  const response = await fetch(`http://localhost:5000/event/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-On-Behalf-Of": user,
    },
    body: JSON.stringify({
      name,
      start_at,
      end_at,
      description,
      event_picture,
      location: location_,
      reward 
    }),
  });

  if (response.status != 200) {
    body = await response.json();
    return alert(`Algo deu errado - status: ${response.status}, msg: ${body.error}`);
  }

  location.reload();
}

async function save(id) {
  const user = localStorage.getItem("user_id");

  const form = document.querySelector(".form" + id);

  const name = form.elements.name.value;
  const start_at = form.elements.start_at.value;
  const end_at = form.elements.end_at.value;
  const description = form.elements.description.value;
  const event_picture = form.elements.event_picture.value;
  const location_ = form.elements.location.value;
  const reward = parseInt(form.elements.reward.value);

  if (new Date(start_at) > new Date(end_at)){
    return alert(`A data inicial tem que ser maior que a final`);
  }

  const response = await fetch(`http://localhost:5000/event/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-On-Behalf-Of": user,
    },
    body: JSON.stringify({
      name,
      start_at,
      end_at,
      description,
      event_picture,
      location: location_,
      reward 
    }),
  });

  if (response.status != 200) {
    body = await response.json();
    return alert(`Algo deu errado - status: ${response.status}, msg: ${body.error}`);
  }

  location.reload();
}

async function destroy(id) {
  const user = localStorage.getItem("user_id");
  await fetch(`http://localhost:5000/event/${id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "X-On-Behalf-Of": user,
    },
  });

  location.reload();
}
