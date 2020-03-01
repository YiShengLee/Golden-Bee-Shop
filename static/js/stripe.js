$(function() {
    // #1 - when form is submitted, this will happen
    $("#payment-form").submit(function() {
        var form = this;
        var card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };
    
    //  this token below is created by stripe from card above
    Stripe.createToken(card, function(status, response) {
        // status 200 means no error
        if (status === 200) {
            $("#credit-card-errors").hide();
            // save the token from stripe (response.id) as the value for the hidden field
            $("#id_stripe_id").val(response.id); 

            // Prevent the credit card details from being submitted to our server
            $("#id_credit_card_number").removeAttr('name');
            $("#id_cvv").removeAttr('name');
            $("#id_expiry_month").removeAttr('name');
            $("#id_expiry_year").removeAttr('name');
            
            // the above credit card detail is removed, then we'll save the form to our database
            form.submit();
            
            // if status is not 200, there's error. Error message will be shown
        } else { 
            $("#stripe-error-message").text(response.error.message);
            $("#credit-card-errors").show();
            $("#validate_card_btn").attr("disabled", false);
        }
    });
    return false;
    });
});