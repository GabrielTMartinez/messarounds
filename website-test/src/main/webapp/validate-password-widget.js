$(function() {
  $.widget( "custom.validatePassword", {
    options: {
      passwordConfirmation: null,
      validationsDiv: $("#password_validations"),
      validations: {
    	  minUppercaseChars: {
              message: "At least one uppercase letter",
              regex: "^(?=.*[A-Z]+).+$"},
          minLowercaseChars: {
              message: "At least one lowercase letter",
              regex: "^(?=.*[a-z]+).+$"},
          minNumbers: {
              message: "At least one number",
              regex: "^(?=.*[0-9]+).+$"},
          minSpecialChars: {
              message: "At least one special letter (!$%@#)",
              regex: "^(?=.*[!$%@#]+).+$"},
          minLength: {
              message: "At least 8 characters",
              regex: ".{8,}$"}
      },
      submitButton: null
    },

    _create: function(){

      if (this.options.passwordConfirmation == null){
        var confirmationField = this.element.data('confirmation-field');
        if (confirmationField != undefined && $(confirmationField).size() >0) {
          this.options.passwordConfirmation = $(confirmationField);
        }
      }

      if (this.options.submitButton == null) {
        var submitButton = this.element.data('submit-button');
        if (submitButton != undefined && $(submitButton).size() >0) {
          this.options.submitButton = $(submitButton);
        }
      }

      this._refresh();
      this.element.keyup(function (){
        $(this).validatePassword("validate");
      });

            this.validate();
    },

    _createValidationsDiv: function(div, validations){
      for(var key in validations){
        var div = this._createValidationRow(key);
        div.append(validations[key].message);
      }
    },

    _createValidationRow: function(id){
      div = "<div class='row' id=\""+id+"\" ><i id=\""+id+"Icon\" class=\"validate-password-icon fa fa-times\"></i></div>";
      this.options.validationsDiv.append(div);
      return $("#"+id);
    },

    _refresh: function(){
      if( this.options.validationsDiv != null) {
        this._createValidationsDiv(this.options.validationsDiv, this.options.validations);
      }

      if(this.options.passwordConfirmation != null) {
        this.options.passwordConfirmation.keyup(function(){
          $(this).data('passwordField').validatePassword("validate");
        });
        this.options.passwordConfirmation.data('passwordField', this.element);
      }

    },

    _destroy: function(){
    },

    _setOptions: function(){
      this._superApply(arguments);
      this._refresh();
    },

    _setOption: function(key, value){
      this._super(key, value);
    },

    validate: function(){
      var isValid = true;
      value = this.element.val();
      for(validation in this.options.validations){
        regexp = new RegExp(this.options.validations[validation].regex);
        var validationResult = regexp.test(value);
        this._setEvaluationResult(validation, validationResult);

        if(!validationResult){
          isValid = false;
        }
      }

      if(!this._validateConfirmation(this.options.passwordConfirmation)) isValid = false;

      if(!isValid){
        this.element.css('border-color', 'red');
        this._disableSubmitButton(this.options.submitButton);
      }else{
        this.element.css('border-color', 'green');
        this._enableSubmitButton(this.options.submitButton);
      }
      return isValid;
    },

    _validateConfirmation: function(confirmationField){
      if (confirmationField == null) return true;

      value = this.element.val();
      confirmationValue = confirmationField.val();
      if(value == confirmationValue && confirmationValue.length > 0){
        confirmationField.css('border-color', 'green');
        return true;
      }else{
        confirmationField.css('border-color', 'red');
        return false;
      }
    },

    _disableSubmitButton: function(submitButton){
      if (submitButton != null) submitButton.attr('disabled','disabled');
    },

    _enableSubmitButton: function(submitButton){
      if (submitButton != null) submitButton.removeAttr('disabled');
    },

    _setEvaluationResult: function(validation, result){
      var div = $("#"+validation);
      var icon = $("#"+validation+"Icon");
      if(result){
        div.css('color', 'green');
        icon.removeClass("fa-times").addClass("fa-check");
      }else{
        div.css('color', 'red');
        icon.removeClass("fa-check").addClass("fa-times");
      }
    },

  });
});