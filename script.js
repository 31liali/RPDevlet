// script.js

import {
    auth,
    db,
    createUserWithEmailAndPassword,
    signInWithEmailAndPassword,
    doc,
    setDoc,
    onAuthStateChanged
} from "./firebase.js";


// Sayfa geçişleri

window.showRegister = function(){

    document.getElementById("loginPage").style.display = "none";

    document.getElementById("registerPage").style.display = "block";

};


window.showLogin = function(){

    document.getElementById("registerPage").style.display = "none";

    document.getElementById("loginPage").style.display = "block";

};



// Zaten giriş yaptıysa direkt girsin

onAuthStateChanged(auth,(user)=>{

    if(user){

        if(location.pathname.endsWith("index.html") || location.pathname === "/"){

            window.location.href="home.html";

        }

    }

});




// Kayıt

window.register = async function(){


    const username =
    document.getElementById("regUser").value
    .trim()
    .toLowerCase();


    const password =
    document.getElementById("regPass").value;


    const password2 =
    document.getElementById("regPass2").value;



    if(username.length < 3){

        alert("Kullanıcı adı en az 3 karakter olmalı.");
        return;

    }


    if(password.length < 8){

        alert("Şifre en az 8 karakter olmalı.");
        return;

    }


    if(password !== password2){

        alert("Şifreler aynı değil.");
        return;

    }



    const fakeEmail =
    username + "@rpdevlet.app";



    try{


        const userCredential =
        await createUserWithEmailAndPassword(
            auth,
            fakeEmail,
            password
        );


        await setDoc(
            doc(
                db,
                "users",
                userCredential.user.uid
            ),
            {

                username: username,

                balance: 0,

                admin:false,

                createdAt:new Date(),

                profile:{

                    name:"",
                    surname:"",
                    birthDate:"",
                    phone:""

                }

            }

        );



        alert("Hesap oluşturuldu!");

        window.location.href="home.html";



    }catch(error){


        alert(error.message);


    }


};





// Giriş

window.login = async function(){


    const username =
    document.getElementById("loginUser").value
    .trim()
    .toLowerCase();



    const password =
    document.getElementById("loginPass").value;



    const fakeEmail =
    username + "@rpdevlet.app";



    try{


        await signInWithEmailAndPassword(

            auth,

            fakeEmail,

            password

        );


        window.location.href="home.html";



    }catch(error){


        alert("Kullanıcı adı veya şifre yanlış.");

    }


};