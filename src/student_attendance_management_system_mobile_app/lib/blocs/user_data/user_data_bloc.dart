import 'dart:async';
import 'dart:developer';

import 'package:meta/meta.dart';
import 'package:bloc/bloc.dart';
import 'package:sams/blocs/user_data/user_data_event.dart';
import 'package:sams/blocs/user_data/user_data_state.dart';
import 'package:sams/models/user_info.dart';
import 'package:sams/services/rest_ds.dart';


class UserDataBloc extends Bloc<UserDataEvent, UserDataState> {
  final RestDatasource api=RestDatasource();

  UserDataState get initialState => UserDataInitial();

    @override
    Stream<UserDataState> mapEventToState( UserDataEvent event,) async* {

      if (event is UserDataInitiate) {
        //TODO: Implement getting data from cache memory 
        yield UserDataLoading();
        try{
          UserInfo userInfo=await api.getUserData();
          await Future<dynamic>.delayed(const Duration(milliseconds: 5000));
          yield UserDataSuccess(userInfo: userInfo);
        }
        catch(error){
          yield UserDataFailure(error: error);
        }
      }
    }
}
