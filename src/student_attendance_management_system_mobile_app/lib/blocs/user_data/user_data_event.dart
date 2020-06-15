
import 'package:meta/meta.dart';
import 'package:equatable/equatable.dart';
import 'package:sams/models/user_info.dart';

abstract class UserDataEvent extends Equatable {
  const UserDataEvent();

  @override
  List<Object> get props => [];
}

class UserDataInitiate extends UserDataEvent {}

class UserInfoReceived extends UserDataEvent {
  final UserInfo userInfo;

  const UserInfoReceived({@required this.userInfo});

  @override
  List<Object> get props => [userInfo];

}