import { ChevronRight } from 'lucide-react';

interface WelcomePageProps {
  onGetStarted: () => void;
}

export default function WelcomePage({ onGetStarted }: WelcomePageProps) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50 flex flex-col items-center justify-center p-6">
      {/* Main Content */}
      <div className="text-center max-w-xl">
        <h1 className="text-5xl font-bold text-gray-900 mb-6">Welcome to Smart Advisors</h1>
        <p className="text-gray-700 text-lg mb-10">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac eros ut nisl convallis 
          feugiat. Suspendisse potenti. {/* replace with real instructions later */}
        </p>

        <button
        onClick={onGetStarted}
        className="mt-10 px-8 py-4 bg-blue-600 text-white font-semibold rounded-xl shadow-lg hover:bg-blue-700 hover:shadow-xl flex items-center justify-center transition-all mx-auto"
        >
        Get Started
        <ChevronRight className="w-5 h-5 ml-2" />
        </button>
      </div>
    </div>
  );
}
