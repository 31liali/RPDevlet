import {
    auth,
    db
} from "./firebase.js";


import {
    createUserWithEmailAndPassword,
    signInWithEmailAndPassword
} from "https://www.gstatic.com/firebasejs/12.0.0/firebase-auth.js";


import {
    doc,
    setDoc
} from "https://www.gstatic.com/firebasejs/12.0.0/firebase-firestore.js";



// Sayfa değiştirme

window.showRegister = function(){

    document.getElementById("loginPage").style.display="none";

    document.getElementById("registerPage").style.display="block";

};



window.showLogin = function(){

    document.getElementById("registerPage").style.display="none";

    document.getElementById("loginPage").style.display="block";

};





// KAYIT

window.register = async function(){


    const username =
    document.getElementById("regUser")
    .value
    .trim()
    .toLowerCase();



    const password =
    document.getElementById("regPass")
    .value;



    const password2 =
    document.getElementById("regPass2")
    .value;



    if(password !== password2){

        alert("Şifreler aynı değil.");
        return;

    }



    if(username.length < 3){

        alert("Kullanıcı adı kısa.");
        return;

    }



    const email =
    username + "@rpdevlet.app";



    try{


        const result =
        await createUserWithEmailAndPassword(
            auth,
            email,
            password
        );



        await setDoc(

            doc(
                db,
                "users",
                result.user.uid
            ),

            {

                username: username,

                balance:0,

                admin:false,

                createdAt:new Date()

            }

        );



        alert("Kayıt başarılı.");

        location.href="home.html";



    }
    catch(error){

        alert(error.message);

    }


};






// GİRİŞ

window.login = async function(){


    const username =
    document.getElementById("loginUser")
    .value
    .trim()
    .toLowerCase();



    const password =
    document.getElementById("loginPass")
    .value;



    const email =
    username + "@rpdevlet.app";



    try{


        await signInWithEmailAndPassword(

            auth,

            email,

            password

        );



        location.href="home.html";


    }
    catch(error){


        alert(
            "Kullanıcı adı veya şifre yanlış."
        );


        console.log(error);

    }


};