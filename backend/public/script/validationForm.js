const LogValidator = () => {
  let logUserName = document.forms["form-login"]["username"];
  let logPassword = document.forms["form-login"]["userPassward"];
  if (logUserName.value == "") {
    logUserName.placeholder = "Please complete this field";
    logUserName.focus();
    return false;
  }

  if (logPassword.value == "") {
    logPassword.placeholder = "Please complete this field";
    logPassword.focus();
    return false;
  }
};

const Validator = () => {
  let inputName = document.forms["form-register"]["name"];
  let inputUserName = document.forms["form-register"]["username"];
  let inputUserPassword = document.forms["form-register"]["userPassword"];
  let inputUserPasswordRetype =
    document.forms["form-register"]["userPasswordRetype"];

  if (inputName.value == "") {
    inputName.placeholder = "Please complete this field";
    inputName.focus();
    return false;
  }
  if (inputUserName.value == "") {
    inputUserName.placeholder = "Please complete this field";
    inputUserName.focus();
    return false;
  }
  if (inputUserName.value.indexOf(" ") >= 0) {
    inputUserName.value = "";
    inputUserName.placeholder = "Unsupported characters";
    inputUserName.focus();
    return false;
  }
  if (inputUserPassword.value == "") {
    inputUserPassword.placeholder = "Please complete this field";
    inputUserPassword.focus();
    return false;
  }
  if (inputUserPassword.value.length < 8) {
    inputUserPassword.value = "";
    inputUserPasswordRetype.value = "";
    inputUserPassword.placeholder = "Password should be more than 8 characters";
    inputUserPassword.focus();
    return false;
  }
  if (inputUserPassword.value.indexOf(" ") >= 0) {
    inputUserPassword.value = "";
    inputUserPasswordRetype.value = "";
    inputUserPassword.placeholder = "Unsupported characters";
    inputUserPassword.focus();
    return false;
  }
  if (inputUserPasswordRetype.value == "") {
    inputUserPasswordRetype.placeholder = "Please complete this field";
    inputUserPasswordRetype.focus();
    return false;
  }
  if (inputUserPasswordRetype.value != inputUserPassword.value) {
    inputUserPasswordRetype.value = "";
    inputUserPasswordRetype.placeholder = "password not match";
    inputUserPasswordRetype.focus();
    return false;
  }
};
