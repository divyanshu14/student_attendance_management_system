import 'package:meta/meta.dart';
import 'package:equatable/equatable.dart';
import 'package:sams/models/user_info.dart';

abstract class UserDataState extends Equatable {
  const UserDataState();

  @override
  List<Object> get props => [];
}

class UserDataInitial extends UserDataState {}

class UserDataLoading extends UserDataState {}

class UserDataSuccess extends UserDataState{
  final UserInfo userInfo;
  const UserDataSuccess({@required this.userInfo});
  @override
  List<Object> get props => [userInfo];
}

class UserDataFailure extends UserDataState {
  final String error;

  const UserDataFailure({@required this.error});

  @override
  List<Object> get props => [error];

  @override
  String toString() => 'ReceiveFailure { error: $error }';
}