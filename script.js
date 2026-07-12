import {
    auth,
    db,
    createUserWithEmailAndPassword,
    signInWithEmailAndPassword,
    doc,
    setDoc
} from "./firebase.js";

// ==========================
// Sayfa Değiştirme
// ==========================

window.showRegister = function () {
    document.getElementById("loginPage").style.display = "none";
    document.getElementById("registerPage").style.display = "block";
};

window.showLogin = function () {
    document.getElementById("registerPage").style.display = "none";
    document.getElementById("loginPage").style.display = "block";
};

// ==========================
// Kayıt
// ==========================

window.register = async function () {

    const username = document.getElementById("regUser").value.trim().toLowerCase();
    const password = document.getElementById("regPass").value;
    const password2 = document.getElementById("regPass2").value;

    if (username.length < 3) {
        alert("Kullanıcı adı en az 3 karakter olmalı.");
        return;
    }

    if (password !== password2) {
        alert("Şifreler uyuşmuyor.");
        return;
    }

    try {

        const email = username + "@rpdevlet.app";

        const result = await createUserWithEmailAndPassword(
            auth,
            email,
            password
        );

        await setDoc(
            doc(db, "users", result.user.uid),
            {
                username: username,
                balance: 0,
                role: "Vatandaş",
                admin: false,
                createdAt: Date.now()
            }
        );

        location.href = "home.html";

    } catch (err) {

        console.error(err);
        alert(err.message);

    }

};

// ==========================
// Giriş
// ==========================

window.login = async function () {

    const username = document.getElementById("loginUser").value.trim().toLowerCase();
    const password = document.getElementById("loginPass").value;

    try {

        await signInWithEmailAndPassword(
            auth,
            username + "@rpdevlet.app",
            password
        );

        location.href = "home.html";

    } catch (err) {

        console.error(err);
        alert("Kullanıcı adı veya şifre yanlış.");

    }

};
