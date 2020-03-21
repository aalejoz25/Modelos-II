function guardarDatos() {
    localStorage.profileimage = document.getElementById("image").value;
    /*Guarda datos basicos*/
    localStorage.nombre = document.getElementById("nombre").value;
    localStorage.celular = document.getElementById("cel").value;
    localStorage.email = document.getElementById("mail").value;
    localStorage.idN = document.getElementById("idN").value;
    localStorage.edad = document.getElementById("age").value;
    /*guarda datos de perfil laboral*/
    localStorage.profile = document.getElementById("profile").value;
    /*Guarda datos de informacion academica*/
    localStorage.nivelestudios = document.getElementById("nivel_estudios").value;
    localStorage.institucion = document.getElementById("institucion").value;
    localStorage.tiempo = document.getElementById("tiempoA").value;
    localStorage.academic1 = document.getElementById("logro1").value;
    localStorage.academic2 = document.getElementById("logro2").value;
    localStorage.academic3 = document.getElementById("logro3").value;
    /*Guarda datos de experiencia laboral */
    localStorage.labor = document.getElementById("labor").value;
    localStorage.empresa = document.getElementById("lugar").value;
    localStorage.boss = document.getElementById("jefe").value;
    localStorage.labtime = document.getElementById("tiempoL").value;
    localStorage.position1 = document.getElementById("cargo1").value;
    localStorage.position2 = document.getElementById("cargo2").value;
    localStorage.position3 = document.getElementById("cargo3").value;
    /*Guarda datos de referencia personal */
    localStorage.prname = document.getElementById("rname").value;
    localStorage.prjob = document.getElementById("rcargo").value;
    localStorage.prphone = document.getElementById("rphone").value;
    /*Guarda datos de referencia familiar */
    localStorage.frname = document.getElementById("fname").value;
    localStorage.fjob = document.getElementById("fcargo").value;
    localStorage.fphone = document.getElementById("fphone").value;

    document.getElementById("saveconfirm").innerHTML = "Sus datos se han guardado en Localstorage";
}


function obtenerdatos() {
    /*inserta datos basicos*/
    document.getElementById("tt").innerHTML = "HV ".concat(localStorage.nombre);
    document.getElementById("name").innerHTML = localStorage.nombre;
    document.getElementById("cel").innerHTML = '<span class="note">Cel: </span>'.concat(localStorage.celular);
    document.getElementById("mail").innerHTML = '<span class="note">e-mail: </span>'.concat(localStorage.email);
    document.getElementById("CC").innerHTML = '<span class="note">Identificación: </span>'.concat(localStorage.idN);
    document.getElementById("age").innerHTML = '<span class="note">Edad: </span>'.concat(localStorage.edad).concat(" años");
    /*inserta perfil laboral*/
    document.getElementById("descripcion").innerHTML = localStorage.profile;
    /*inserta datos informacion academica*/
    document.getElementById("nivel").innerHTML = localStorage.nivelestudios;
    document.getElementById("inst").innerHTML = localStorage.institucion;
    document.getElementById("time").innerHTML = localStorage.tiempo;
    document.getElementById("d1").innerHTML = localStorage.academic1;
    document.getElementById("d2").innerHTML = localStorage.academic2;
    document.getElementById("d3").innerHTML = localStorage.academic3;
    /*inserta datos de informacion laboral*/
    document.getElementById("labor").innerHTML = localStorage.labor;
    document.getElementById("place").innerHTML = localStorage.empresa;
    document.getElementById("boss").innerHTML = localStorage.boss;
    document.getElementById("ltime").innerHTML = localStorage.labtime;
    document.getElementById("c1").innerHTML = localStorage.position1;
    document.getElementById("c2").innerHTML = localStorage.position2;
    document.getElementById("c3").innerHTML = localStorage.position3;
    /*inserta datos de referencia personal*/
    document.getElementById("rname").innerHTML = localStorage.prname;
    document.getElementById("rjob").innerHTML = localStorage.prjob;
    document.getElementById("rcel").innerHTML = localStorage.prphone;
    /*inserta datos de referencia personal*/
    document.getElementById("fname").innerHTML = localStorage.frname;
    document.getElementById("fjob").innerHTML = localStorage.fjob;
    document.getElementById("fcel").innerHTML = localStorage.fphone;

}