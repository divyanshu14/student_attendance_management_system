
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:sams/blocs/authentication/authentication_event.dart';
import 'package:sams/blocs/authentication/authentication_state.dart';
import 'package:sams/services/user_token.dart';

class AuthenticationBloc extends Bloc<AuthenticationEvent, AuthenticationState> {
  AuthenticationBloc();

  @override
  AuthenticationState get initialState => AuthenticationUninitialized();

  
@override
Stream<AuthenticationState> mapEventToState( AuthenticationEvent event,) async* {
  
  if (event is AppStarted) {
    final bool hasToken = await UserToken.fetchToken();

    if (hasToken) {
      yield AuthenticationAuthenticated();
    } else {
      yield AuthenticationUnauthenticated();
    }
  }

  if (event is LoggedIn) {
    yield AuthenticationLoading();
    await UserToken.persistToken(event.token);
    yield AuthenticationAuthenticated();
  }

  if (event is LoggedOut) {
    yield AuthenticationLoading();
    await UserToken.removeToken();
    yield AuthenticationUnauthenticated();
  }
}

}