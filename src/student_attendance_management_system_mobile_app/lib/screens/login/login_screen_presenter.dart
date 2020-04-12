import 'dart:developer';

import 'package:sams/data/rest_ds.dart';
import 'package:sams/models/user.dart';

abstract class LoginScreenContract {
  void onLoginSuccess(User user);
  void onLoginError(String errorTxt);
}

class LoginScreenPresenter {
  LoginScreenContract _view;
  RestDatasource _api = new RestDatasource();
  LoginScreenPresenter(this._view);

  doLogin(String username, String password) {
    _api.login(username, password).then((User user) {
      log('success');
      _view.onLoginSuccess(user);
    }).catchError((dynamic error) {
      log('unsuccessful');
    _view.onLoginError(error.toString());
    } );
  }
}