async function handleSubmit(event) {
  event.preventDefault();
  const data = new FormData(event.target);
  const login = data.get("login");
  const password = data.get("password");
  
  await fetch("http://localhost:5000/user/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ login, password }),
  });
}

const form = document.querySelector("form");
form.addEventListener("submit", handleSubmit);
