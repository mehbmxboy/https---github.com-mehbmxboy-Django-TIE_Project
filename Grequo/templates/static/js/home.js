$(document).ready(function () {
  $("#buttonSubmitID").click(function () {
    var databack = $("#myModal #questionInput").val().trim();
    $("#result").html(databack);
  });
});

window.onload = function () {
  Particles.init({
    selector: ".background",
  });
};
