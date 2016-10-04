var getButtonLayout = function() {
  $.ajax({
    url: "http://localhost:8080/api/controllers",
    processData: true,
    data: {},
    dataType: "json",
    success: function(data) {
      $("#messages").text(data.xbox.buttons.x);
      console.log(data.xbox);
      },
    error: function(err1,err2) {
      $("#messages").text(err2);
    }
  });
});