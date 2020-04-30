import 'dart:async';

import 'package:meta/meta.dart';
import 'package:bloc/bloc.dart';
import 'package:sams/blocs/authentication/authentication_bloc.dart';
import 'package:sams/blocs/authentication/authentication_event.dart';
import 'package:sams/blocs/login/login_events.dart';
import 'package:sams/blocs/login/login_state.dart';
import 'package:sams/services/rest_ds.dart';


class LoginBloc extends Bloc<LoginEvent, LoginState> {
  final RestDatasource api=RestDatasource();
  final AuthenticationBloc authenticationBloc;

  LoginBloc({
    @required this.authenticationBloc,
  })  : assert(authenticationBloc != null);

  LoginState get initialState => LoginInitial();

  @override
  Stream<LoginState> mapEventToState(LoginEvent event) async* {
    if (event is LoginButtonPressed) {
      yield LoginLoading();
      try {
        final token = await api.login(
          event.email,
          event.password,
        );
        authenticationBloc.add(LoggedIn(token: token));
        yield LoginInitial();
      } catch (error) {
        yield LoginFailure(error: error.toString());
      }
    }
  }
}
