import { Star, Users, Calendar, TrendingUp, Clock, Award, BookOpen, Filter } from 'lucide-react';

interface Professor {
  id: string;
  name: string;
  rating: number;
  reviewCount: number;
  course: string;
  courseCode: string;
  difficulty: string;
  matchScore: number;
  schedule: string;
  classSize: string;
  assessmentType: string;
  attendance: string;
  tags: string[];
}

export default function RecommendationDashboard() {
  const mockProfessors: Professor[] = [
    {
      id: '1',
      name: 'Dr. Sarah Chen',
      rating: 4.8,
      reviewCount: 234,
      course: 'Fluid Mechanics',
      courseCode: 'CE 201',
      difficulty: 'Moderate',
      matchScore: 98,
      schedule: 'Mon/Wed 2:00-3:30 PM',
      classSize: 'Small (25)',
      assessmentType: 'Assignment Heavy',
      attendance: 'Not Required',
      tags: ['Clear Explanations', 'Helpful', 'Fair Grader'],
    },
    {
      id: '2',
      name: 'Prof. Michael Rodriguez',
      rating: 4.6,
      reviewCount: 189,
      course: 'Engineering Graphics and Drawing',
      courseCode: 'CE 305',
      difficulty: 'Moderate',
      matchScore: 95,
      schedule: 'Tue/Thu 10:00-11:30 AM',
      classSize: 'Medium (40)',
      assessmentType: 'Balanced',
      attendance: 'Required',
      tags: ['Engaging', 'Real-world Examples', 'Responsive'],
    },
    {
      id: '3',
      name: 'Dr. Emily Watson',
      rating: 4.9,
      reviewCount: 312,
      course: 'Soil Mechanics',
      courseCode: 'CE 401',
      difficulty: 'Challenging',
      matchScore: 92,
      schedule: 'Mon/Wed 4:00-5:30 PM',
      classSize: 'Small (30)',
      assessmentType: 'Assignment Heavy',
      attendance: 'Not Required',
      tags: ['Industry Expert', 'Practical Projects', 'Inspiring'],
    },
  ];

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty.toLowerCase()) {
      case 'easy': return 'text-green-700 bg-green-50';
      case 'moderate': return 'text-yellow-700 bg-yellow-50';
      case 'challenging': return 'text-orange-700 bg-orange-50';
      default: return 'text-gray-700 bg-gray-50';
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50">
      <nav className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <div className="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center mr-3">
                <Award className="w-6 h-6 text-white" />
              </div>
              <h1 className="text-xl font-bold text-gray-900">Smart Advisors</h1>
            </div>
            <div className="flex items-center gap-4">
              <button className="px-4 py-2 text-gray-600 hover:text-gray-900 font-medium">
                Dashboard
              </button>
              <button className="px-4 py-2 text-gray-600 hover:text-gray-900 font-medium">
                My Schedule
              </button>
              <div className="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
                <span className="text-blue-700 font-semibold">JD</span>
              </div>
            </div>
          </div>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto px-6 py-8">
        <div className="mb-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-2">Your Recommended Professors</h2>
          <p className="text-gray-600">Based on your transcript and preferences, here are your top matches</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6 mb-6">
          <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600 mb-1">Courses Analyzed</p>
                <p className="text-2xl font-bold text-gray-900">12</p>
              </div>
              <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                <BookOpen className="w-6 h-6 text-blue-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600 mb-1">Matches Found</p>
                <p className="text-2xl font-bold text-gray-900">24</p>
              </div>
              <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
                <TrendingUp className="w-6 h-6 text-green-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600 mb-1">Avg Match Score</p>
                <p className="text-2xl font-bold text-gray-900">95%</p>
              </div>
              <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
                <Star className="w-6 h-6 text-purple-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600 mb-1">Avg Rating</p>
                <p className="text-2xl font-bold text-gray-900">4.7</p>
              </div>
              <div className="w-12 h-12 bg-yellow-100 rounded-lg flex items-center justify-center">
                <Award className="w-6 h-6 text-yellow-600" />
              </div>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-6 mb-6">
          <div className="flex items-center justify-between">
            <h3 className="text-lg font-semibold text-gray-900">Filter Results</h3>
            <button className="text-blue-600 hover:text-blue-700 font-medium text-sm">
              Reset Filters
            </button>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mt-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                <Filter className="w-4 h-4 inline mr-1" />
                Course Level
              </label>
              <select className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
                <option>All Levels</option>
                <option>100-200</option>
                <option>300-400</option>
                <option>500+</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Min Rating
              </label>
              <select className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
                <option>Any Rating</option>
                <option>4.5+</option>
                <option>4.0+</option>
                <option>3.5+</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Difficulty
              </label>
              <select className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
                <option>All</option>
                <option>Easy</option>
                <option>Moderate</option>
                <option>Challenging</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Time of Day
              </label>
              <select className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none">
                <option>Any Time</option>
                <option>Morning</option>
                <option>Afternoon</option>
                <option>Evening</option>
              </select>
            </div>
          </div>
        </div>

        <div className="space-y-4">
          {mockProfessors.map((professor) => (
            <div
              key={professor.id}
              className="bg-white rounded-xl shadow-sm border border-gray-100 p-6 hover:shadow-md transition-shadow"
            >
              <div className="flex items-start justify-between mb-4">
                <div className="flex-1">
                  <div className="flex items-center gap-3 mb-2">
                    <h3 className="text-xl font-bold text-gray-900">{professor.name}</h3>
                    <div className="px-3 py-1 bg-blue-600 text-white rounded-full text-sm font-semibold">
                      {professor.matchScore}% Match
                    </div>
                  </div>
                  <div className="flex items-center gap-4 text-sm text-gray-600">
                    <span className="font-medium text-blue-600">{professor.courseCode}</span>
                    <span>{professor.course}</span>
                  </div>
                </div>
                <div className="text-right">
                  <div className="flex items-center gap-1 mb-1">
                    <Star className="w-5 h-5 text-yellow-500 fill-yellow-500" />
                    <span className="text-xl font-bold text-gray-900">{professor.rating}</span>
                  </div>
                  <p className="text-xs text-gray-500">{professor.reviewCount} reviews</p>
                </div>
              </div>

              <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-4">
                <div className="flex items-start gap-2">
                  <Clock className="w-4 h-4 text-gray-400 mt-0.5" />
                  <div>
                    <p className="text-xs text-gray-500">Schedule</p>
                    <p className="text-sm font-medium text-gray-900">{professor.schedule}</p>
                  </div>
                </div>
                <div className="flex items-start gap-2">
                  <Users className="w-4 h-4 text-gray-400 mt-0.5" />
                  <div>
                    <p className="text-xs text-gray-500">Class Size</p>
                    <p className="text-sm font-medium text-gray-900">{professor.classSize}</p>
                  </div>
                </div>
                <div className="flex items-start gap-2">
                  <BookOpen className="w-4 h-4 text-gray-400 mt-0.5" />
                  <div>
                    <p className="text-xs text-gray-500">Assessment</p>
                    <p className="text-sm font-medium text-gray-900">{professor.assessmentType}</p>
                  </div>
                </div>
                <div className="flex items-start gap-2">
                  <Calendar className="w-4 h-4 text-gray-400 mt-0.5" />
                  <div>
                    <p className="text-xs text-gray-500">Attendance</p>
                    <p className="text-sm font-medium text-gray-900">{professor.attendance}</p>
                  </div>
                </div>
              </div>

              <div className="flex items-center justify-between pt-4 border-t">
                <div className="flex items-center gap-2">
                  <span className={`px-3 py-1 rounded-full text-xs font-medium ${getDifficultyColor(professor.difficulty)}`}>
                    {professor.difficulty}
                  </span>
                  {professor.tags.slice(0, 3).map((tag, index) => (
                    <span key={index} className="px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-xs font-medium">
                      {tag}
                    </span>
                  ))}
                </div>
                <button className="px-6 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition-colors">
                  View Details
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
