// Generated by gencpp from file graph_d_exploration/InfoMatrix.msg
// DO NOT EDIT!


#ifndef GRAPH_D_EXPLORATION_MESSAGE_INFOMATRIX_H
#define GRAPH_D_EXPLORATION_MESSAGE_INFOMATRIX_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace graph_d_exploration
{
template <class ContainerAllocator>
struct InfoMatrix_
{
  typedef InfoMatrix_<ContainerAllocator> Type;

  InfoMatrix_()
    : rows(0)
    , data()  {
    }
  InfoMatrix_(const ContainerAllocator& _alloc)
    : rows(0)
    , data(_alloc)  {
  (void)_alloc;
    }



   typedef uint32_t _rows_type;
  _rows_type rows;

   typedef std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> _data_type;
  _data_type data;





  typedef boost::shared_ptr< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> const> ConstPtr;

}; // struct InfoMatrix_

typedef ::graph_d_exploration::InfoMatrix_<std::allocator<void> > InfoMatrix;

typedef boost::shared_ptr< ::graph_d_exploration::InfoMatrix > InfoMatrixPtr;
typedef boost::shared_ptr< ::graph_d_exploration::InfoMatrix const> InfoMatrixConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::graph_d_exploration::InfoMatrix_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::graph_d_exploration::InfoMatrix_<ContainerAllocator1> & lhs, const ::graph_d_exploration::InfoMatrix_<ContainerAllocator2> & rhs)
{
  return lhs.rows == rhs.rows &&
    lhs.data == rhs.data;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::graph_d_exploration::InfoMatrix_<ContainerAllocator1> & lhs, const ::graph_d_exploration::InfoMatrix_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace graph_d_exploration

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c56ec7891acf134bf7f478b29ade73c5";
  }

  static const char* value(const ::graph_d_exploration::InfoMatrix_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc56ec7891acf134bULL;
  static const uint64_t static_value2 = 0xf7f478b29ade73c5ULL;
};

template<class ContainerAllocator>
struct DataType< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> >
{
  static const char* value()
  {
    return "graph_d_exploration/InfoMatrix";
  }

  static const char* value(const ::graph_d_exploration::InfoMatrix_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Matrix of type [Reward, X, Y] with dimensions [nx3]\n"
"uint32 rows\n"
"float32[] data\n"
;
  }

  static const char* value(const ::graph_d_exploration::InfoMatrix_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.rows);
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct InfoMatrix_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::graph_d_exploration::InfoMatrix_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::graph_d_exploration::InfoMatrix_<ContainerAllocator>& v)
  {
    s << indent << "rows: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.rows);
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // GRAPH_D_EXPLORATION_MESSAGE_INFOMATRIX_H