// =========================
// RPDevlet v1
// script.js
// =========================

// Admin Bilgileri
const ADMIN_USER = "A.B";
const ADMIN_PASS = "A.B41";

// Kullanıcıları yükle
let users = JSON.parse(localStorage.getItem("rp_users")) || [];

// ----------------------
// Giriş
// ----------------------
function login(){

    const user = document.getElementById("loginUser").value.trim();
    const pass = document.getElementById("loginPass").value;

    // Admin kontrolü
    if(user === ADMIN_USER && pass === ADMIN_PASS){

        window.location.href = "admin.html";
        return;

    }

    // Normal kullanıcı
    const account = users.find(u => u.username === user && u.password === pass);

    if(account){

        localStorage.setItem("loggedUser", JSON.stringify(account));

        window.location.href = "home.html";

    }else{

        alert("❌ Kullanıcı adı veya şifre yanlış.");

    }

}

// ----------------------
// Kayıt
// ----------------------
function register(){

    const username = document.getElementById("regUser").value.trim();
    const email = document.getElementById("regMail").value.trim();
    const pass = document.getElementById("regPass").value;
    const pass2 = document.getElementById("regPass2").value;

    if(username === "" || email === "" || pass === "" || pass2 === ""){

        alert("Lütfen tüm alanları doldurun.");
        return;

    }

    if(pass !== pass2){

        alert("Şifreler uyuşmuyor.");
        return;

    }

    if(username === ADMIN_USER){

        alert("Bu kullanıcı adı kullanılamaz.");
        return;

    }

    if(users.some(u => u.username === username)){

        alert("Bu kullanıcı adı zaten kayıtlı.");
        return;

    }

    const newUser = {

        id: "RP-" + String(users.length + 1).padStart(6,"0"),
        username: username,
        email: email,
        password: pass

    };

    users.push(newUser);

    localStorage.setItem("rp_users", JSON.stringify(users));

    alert("✅ Hesap oluşturuldu.");

    showLogin();

}

// ----------------------
// Sayfa Değiştir
// ----------------------
function showRegister(){

    const login = document.getElementById("loginPage");
    const register = document.getElementById("registerPage");

    if(login && register){

        login.style.display = "none";
        register.style.display = "block";

    }

}

function showLogin(){

    const login = document.getElementById("loginPage");
    const register = document.getElementById("registerPage");

    if(login && register){

        login.style.display = "block";
        register.style.display = "none";

    }

}

// ----------------------
// Çıkış
// ----------------------
function logout(){

    localStorage.removeItem("loggedUser");

    window.location.href = "index.html";

}

// ----------------------
// Home Kontrol
// ----------------------
window.onload = function(){

    if(location.pathname.includes("home.html")){

        const user = JSON.parse(localStorage.getItem("loggedUser"));

        if(!user){

            window.location.href = "index.html";
            return;

        }

    }

}