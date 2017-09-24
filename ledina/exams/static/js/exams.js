$(function () {



$(".prev-btn").on("click", function(){
  current = $(".li-placeholder").find("li.active");
  next = current.prev()
  if (current.index() == 0 ){
    next = $(".li-placeholder li").last();
    src = $(next).attr("src");
    $(".content").attr("src", src);
    $(".download-link").attr("href", src);
    $(next).addClass("active");
    $(current).removeClass("active");
  }
  else {
  src = next.attr("src");
  $(".content").attr("src", src);
  $(".download-link").attr("href", src);
  $(next).addClass("active");
  $(current).removeClass("active");
}
})

$(".next-btn").on("click", function(){
  current = $(".li-placeholder li.active");
  next = current.next()
  if (current.index() == $(".li-placeholder li").last().index()){
    next = $(".li-placeholder li:eq(0)");
    src = $(next).attr("src");
    $(".content").attr("src", src);
    $(".download-link").attr("href", src);
    $(next).addClass("active");
    $(current).removeClass("active");
  }
  else {
  src = next.attr("src");
  $(".content").attr("src", src);
  $(".download-link").attr("href", src);
  $(next).addClass("active");
  $(current).removeClass("active");
}

})


$(".exam-span-file").on("click", function(){
  wrapper = $(this).closest(".exam-span-wrapper");
  src = $(wrapper).find("li:eq(0)").attr("src");
  $(".content").attr("src", src);
  $(".download-link").attr("href", src);
  $(".imgmodal").show();
  exam_id = $(this).closest(".exam-box").attr("data-exam-id");
  $(".imgmodal").attr("data-exam-id", exam_id);
  $(wrapper).find("li:eq(0)").addClass("active");
  clone = $(wrapper).find(".exam-ul").clone();
  $(".li-placeholder").html(clone);

  if ($(".li-placeholder li").length == 1 ){
    $(".prev-btn").hide();
    $(".next-btn").hide();
  }
  else {
    $(".next-btn").show();   
    $(".prev-btn").show(); 
  }


})

$("#files-modal-button").on("click", function(){
  $("#files-modal").modal('show');
})

  $(".comments-modal-button").on("click", function(){
    $('#comments-modal').modal('show'); 
  })

$(".profile-comments").on("click", function() {
  $("#profile-comments-modal").modal("toggle");
})

$(".mark-exam").on("click", function() {
  var exam_mark = this;
  var exam = $(this).closest(".exam-box").attr("data-exam-id");
  var path = $(this).closest(".exam-box").attr("data-path");
  $.ajax({
    url: "/testi/" + path + "/mark_exam",
    data: {
      "exam": exam,
    },
    type: "get",
    cache: false,
    success: function(data){
      if (data.mark == "marked"){
        $(exam_mark).find(".glyphicon-ban-circle").addClass("active");
      }
      else {
        $(exam_mark).find(".glyphicon-ban-circle").removeClass("active");
      }
      console.log(data.mark);
    },
    error: function() {
      $("#snackbar").html("Za ocenjevanje testov se morate prijaviti");
      $("#snackbar").fadeIn().delay(1500).fadeOut();

    }
  })
})

$(".remove-exam").on("click", function() {
  var div = $(this).closest(".exam-box");
  var csrf = $(div).attr("data-csrf");
  var exam = $(div).attr("data-exam-id");
  var path = $(div).attr("data-path");
  if (confirm('Ali ste prepričani, da želite izbrisati ta test?')) {
  $.ajax({
    url: "/testi/" + path + "/remove_exam",
    data: {
      "exam": exam,
      "csrfmiddlewaretoken": csrf
    },
    type: "post",
    cache: false,
    success: function(){
    $(div).fadeOut(400, function () {
          $(div).remove();
        }); 
  if ($(".exam-box-parent .exam-box").length  == 3){
    $(".exam-box").wrapAll("<div class='two-children'></div>")
    }
  }
  })
}

})


$(".comment").on("click", function() {
      var parent = $(this).closest(".exam-box");
      var clearfix = $("#comments-modal-clearfix");
      var exam_id = $(parent).attr("data-exam-id");
      var path = $(parent).attr("data-path");
      console.log(path);
      $.ajax({
        url: "/testi/" + path +"/comment",
        data: {'exam_id': exam_id },
        cache: false,
        success: function (data) {
          $(clearfix).html(data);
          $('#comments-modal').modal('show');
          $( "#modal-exam-id" ).attr( "value", exam_id );
          $("#modal-exam-id").attr("data-path", path);
        }
      })

})
$(".comments input[name='post']").keydown(function (evt) {
    var keyCode = evt.which?evt.which:evt.keyCode;
    $("#comment-helper").fadeIn();
    if (keyCode == 13) {
      var form = $(this).closest("form");
      var container = $(form).closest(".comments");
      var clearfix = $("#comments-modal-clearfix");
      var path = $("#modal-exam-id").attr("data-path");
      var input = this;
      $.ajax({
        url: "/testi/"+ path + "/comment",
        data: $(form).serialize(),
        type: 'post',
        cache: false,
        beforeSend: function () {
          $(input).val("");
          $(input).blur();
        },
        success: function (data) {
          $("#comment-helper").fadeOut();
          $(clearfix).html(data);
          $(clearfix).scrollTop($(clearfix)[0].scrollHeight);
        }

      });
    }
  });

  $("#comments-modal-clearfix").on("click", ".delete-comment", function(){
    var comment_list = $(this).closest(".comment-list");
    var comment_id = $(comment_list).attr("data-comment-pk");
    var csrf = $(this).closest(".comment-list").attr("data-csrf");
    var path = $("#modal-exam-id").attr("data-path");
  $.ajax({
    url: "/testi/" + path + "/remove_comment",
    data: {
      "comment_id": comment_id,
      "csrfmiddlewaretoken": csrf
    },
    type: "post",
    cache: false,
    success: function(){
    $(comment_list).fadeOut(400, function () {
          $(comment_list).remove();
        }); 
    if ($(".comment-list").length == 1 ){
      $("#comments-modal").modal("hide");
    }
  }
  })

  })
  

$("#img-form").on("submit", function(e) {
  e.preventDefault();
  var formData = new FormData(this); 
  if ($("input:file")[0].files.length > 8 ){
    $("#error-div").html("<strong>Naložite lahko največ 8 datotek</strong>")
    $("#error-div").fadeIn();
  }
  else {
  $.ajax({
    url: window.location.pathname + "/dodaj",
    data: formData,
    type: 'post',
    cache: false,
    contentType: false,
    processData: false,

    beforeSend: function(){
      $(".img-form-btn").html('<i class="fa fa-circle-o-notch fa-spin"></i>');
      $('.img-form-btn').attr("disabled", true);
    },
    success:function(data){
      if (data.success){
      $("#myModalHorizontal").modal('hide');
      location.reload();
    }
    else if (data.error){
      $("#error-div").html("<strong>" + data.error + "</strong>");
      $("#error-div").fadeIn();
      $(".img-form-btn").html('Shrani');
      $('.img-form-btn').attr("disabled", false);
    }
    },
    error: function(data){
      alert("Napaka. Preverite povezavo z internetom.");
      $(".img-form-btn").html('Shrani');
    }
  })
}
})

$(".img-form-btn").on("click", function(){
  $("#img-form").submit();
})

$(".letter-accordion").on("click", function() {
  classes_child = $(this).closest(".classes-child");
  panels = $(classes_child).find(".subject-panel");
  span = $(this).find(".plus-minus");
  if ($(this).hasClass("open")){
    $(panels).slideUp();
    $(span).html("+");
    $(this).removeClass("open");
  }
  else {
  $(this).addClass("open");
  $(panels).slideDown();
  $(span).html("-");
}

});

if ($(".exam-box-parent .exam-box").length == 2) {
  $(".exam-box").wrapAll("<div class='two-children'></div>")
}

$(".shut").on("click", function() {
    $(".imgmodal").hide();
    $(".content").attr("src", "");
  })


$("document").ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   
});



});
