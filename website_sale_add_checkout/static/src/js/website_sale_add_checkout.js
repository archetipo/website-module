$(document).ready(function () {

  var oe_website_sale = $('.oe_website_sale');
  var checkout_company_name = $(oe_website_sale).find("#checkout_company_name");
  var label_your_name = $(oe_website_sale).find("#label_your_name");
  var fiscalcode = $(oe_website_sale).find("#fiscalcode_id");
  var vat = $(oe_website_sale).find("#vat_id");
  var partner_type = $('#partner_type');

  function loading(){
        $('button.btn.btn-primary.pull-left').val('Loading...');
        $('button.btn.btn-primary.pull-left').prop('disabled', true);
  }
  function loading_done(){
        $('button.btn.btn-primary.pull-left').val('Confirm');
        $('button.btn.btn-primary.pull-left').prop('disabled', false);
  }

  function checkPartenr(partner_type){
    if (partner_type.val() == "individual"){
        checkout_company_name.show();
        vat.hide();
        label_your_name.html("Nome e Cognome");
    }
    else if (partner_type.val() == "company"){
        checkout_company_name.hide();
        vat.show();
        label_your_name.html("Nome Azienda");
    }
    else if (partner_type.val() == "association"){
        checkout_company_name.hide();
        vat.hide();
        label_your_name.html("Nome Associaizone");
    }
    else if (partner_type.val() == "select"){
        checkout_company_name.show();
        label_your_name.html("Nome / Nome azienda");
    }
  }

  checkPartenr(partner_type);


  $(oe_website_sale).on("change", '#partner_type', function (event) {
      checkPartenr($(event.target));
  });


    $('select#checkout_country').bind('change', function(e) {
      loading();
      var state = $('#state_id');
      if (state) state.remove();
      var country_id = $('select#checkout_country').val();
      $.ajax( {
            type: "GET",
            url: "/web/get_province",
            data: $.param({'token': $.urlParam('token'),'checkout_country': country_id}),
            success: function( response ) {
              if(response!=""){
                  $("div#country_div").after(response);
              }
              loading_done();
            }
      });

    });

});
