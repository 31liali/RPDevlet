// RPDevlet Script

document.addEventListener("DOMContentLoaded", () => {

    console.log("RPDevlet başlatıldı.");

    // Tüm formlarda boş alan kontrolü
    document.querySelectorAll("form").forEach(form => {

        form.addEventListener("submit", function(e){

            let bos = false;

            this.querySelectorAll("input[required], select[required]").forEach(i => {

                if(i.value.trim() === ""){
                    bos = true;
                }

            });

            if(bos){
                e.preventDefault();
                alert("Lütfen tüm alanları doldurun.");
            }

        });

    });

});


// Admin İşlemleri

function paraVerOnay(){

    return confirm("Bu kullanıcıya para vermek istediğinize emin misiniz?");

}

function ehliyetVerOnay(){

    return confirm("Ehliyet verilsin mi?");

}

function tapuVerOnay(){

    return confirm("Tapu verilsin mi?");

}

function cezaKesOnay(){

    return confirm("Ceza kesilsin mi?");

}


// Bildirim

function bildirim(text){

    alert(text);

}