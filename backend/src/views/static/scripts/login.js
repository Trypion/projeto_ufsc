async function handleSubmit(event) {
  event.preventDefault();
  const data = new FormData(event.target);
  const login = data.get("login");
  const password = data.get("password");
  
  const response = await fetch("http://localhost:5000/user/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ login, password }),
  });

  if (response.status == 200){
    const user = await response.json()
    localStorage.setItem("user_id", user.id) 
    document.location.href = '/'   
  }
  else {
    body = await response.json()
    alert(
      `Algo deu errado - status: ${response.status}, msg: ${body.error}`
    );
  }
}

const form = document.querySelector("form");
form.addEventListener("submit", handleSubmit);
