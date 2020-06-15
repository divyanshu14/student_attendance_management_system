import 'package:meta/meta.dart';
import 'package:equatable/equatable.dart';
import 'package:sams/models/course_info.dart';

abstract class CourseInfoState extends Equatable {
  const CourseInfoState();

  @override
  List<Object> get props => [];
}

class CourseInfoInitial extends CourseInfoState {}

class CourseInfoLoading extends CourseInfoState {}

class CourseInfoSuccess extends CourseInfoState{
  final CourseInfo courseInfo;
  const CourseInfoSuccess({@required this.courseInfo});
  @override
  List<Object> get props => [courseInfo];
}

class CourseInfoFailure extends CourseInfoState {
  final String error;

  const CourseInfoFailure({@required this.error});

  @override
  List<Object> get props => [error];

  @override
  String toString() => 'ReceiveFailure { error: $error }';
}