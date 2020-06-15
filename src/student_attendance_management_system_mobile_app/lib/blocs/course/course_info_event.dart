
import 'package:meta/meta.dart';
import 'package:equatable/equatable.dart';
import 'package:sams/models/course_info.dart';

abstract class CourseInfoEvent extends Equatable {
  const CourseInfoEvent();

  @override
  List<Object> get props => [];
}

class CourseInfoInitiate extends CourseInfoEvent {}

class CourseInfoReceived extends CourseInfoEvent {
  final CourseInfo courseInfo;

  const CourseInfoReceived({@required this.courseInfo});

  @override
  List<Object> get props => [courseInfo];

}