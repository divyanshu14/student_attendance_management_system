import 'dart:developer';

import 'package:sams/data/rest_ds.dart';

// handles logic behind login screen

abstract class LoginScreenContract {
  void onLoginSuccess();
  void onLoginError(String errorTxt);
}

class LoginScreenPresenter {
  LoginScreenContract _view;
  RestDatasource _api = new RestDatasource();
  LoginScreenPresenter(this._view);

  doLogin(String username, String password) {
    _api.login(username, password).then((value) {
      log('Login Successful');
      _view.onLoginSuccess();
    }).catchError((Object error) {
      log('Login unsuccessful');
    _view.onLoginError(error.toString());
    } );
  }
}