// Generated by gencpp from file graph_d_exploration/ChooseGoalGoal.msg
// DO NOT EDIT!


#ifndef GRAPH_D_EXPLORATION_MESSAGE_CHOOSEGOALGOAL_H
#define GRAPH_D_EXPLORATION_MESSAGE_CHOOSEGOALGOAL_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <graph_d_exploration/InfoMatrix.h>

namespace graph_d_exploration
{
template <class ContainerAllocator>
struct ChooseGoalGoal_
{
  typedef ChooseGoalGoal_<ContainerAllocator> Type;

  ChooseGoalGoal_()
    : client_id()
    , matrix()
    , rows()  {
    }
  ChooseGoalGoal_(const ContainerAllocator& _alloc)
    : client_id(_alloc)
    , matrix(_alloc)
    , rows(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _client_id_type;
  _client_id_type client_id;

   typedef  ::graph_d_exploration::InfoMatrix_<ContainerAllocator>  _matrix_type;
  _matrix_type matrix;

   typedef std::vector<int8_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int8_t>> _rows_type;
  _rows_type rows;





  typedef boost::shared_ptr< ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> const> ConstPtr;

}; // struct ChooseGoalGoal_

typedef ::graph_d_exploration::ChooseGoalGoal_<std::allocator<void> > ChooseGoalGoal;

typedef boost::shared_ptr< ::graph_d_exploration::ChooseGoalGoal > ChooseGoalGoalPtr;
typedef boost::shared_ptr< ::graph_d_exploration::ChooseGoalGoal const> ChooseGoalGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator1> & lhs, const ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator2> & rhs)
{
  return lhs.client_id == rhs.client_id &&
    lhs.matrix == rhs.matrix &&
    lhs.rows == rhs.rows;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator1> & lhs, const ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace graph_d_exploration

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ccc4eb8941602a0039260071e46f98e1";
  }

  static const char* value(const ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xccc4eb8941602a00ULL;
  static const uint64_t static_value2 = 0x39260071e46f98e1ULL;
};

template<class ContainerAllocator>
struct DataType< ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "graph_d_exploration/ChooseGoalGoal";
  }

  static const char* value(const ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# Action definition for choosing centroids\n"
"# The goal specifies the client id and the matrix with the lists in which each element is of the form [Reward, X, Y]\n"
"# The action server should try to choose the centroid that maximizes the information gain depending on the priority\n"
"# of the robots (r0 > ... > rn)\n"
"\n"
"# Goal definition\n"
"string client_id\n"
"InfoMatrix matrix\n"
"int8[] rows\n"
"\n"
"================================================================================\n"
"MSG: graph_d_exploration/InfoMatrix\n"
"# Matrix of type [Reward, X, Y] with dimensions [nx3]\n"
"uint32 rows\n"
"float32[] data\n"
;
  }

  static const char* value(const ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.client_id);
      stream.next(m.matrix);
      stream.next(m.rows);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ChooseGoalGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::graph_d_exploration::ChooseGoalGoal_<ContainerAllocator>& v)
  {
    s << indent << "client_id: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.client_id);
    s << indent << "matrix: ";
    s << std::endl;
    Printer< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> >::stream(s, indent + "  ", v.matrix);
    s << indent << "rows[]" << std::endl;
    for (size_t i = 0; i < v.rows.size(); ++i)
    {
      s << indent << "  rows[" << i << "]: ";
      Printer<int8_t>::stream(s, indent + "  ", v.rows[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // GRAPH_D_EXPLORATION_MESSAGE_CHOOSEGOALGOAL_H
