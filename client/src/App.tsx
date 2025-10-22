import { useState } from 'react';
import AuthScreen from './components/AuthScreen';
import OnboardingScreen from './components/OnboardingScreen';
import RecommendationDashboard from './components/RecommendationDashboard';

type AppState = 'auth' | 'onboarding' | 'dashboard';

function App() {
  const [appState, setAppState] = useState<AppState>('auth');

  return (
    <>
      {appState === 'auth' && (
        <AuthScreen onAuthSuccess={() => setAppState('onboarding')} />
      )}
      {appState === 'onboarding' && (
        <OnboardingScreen onComplete={() => setAppState('dashboard')} />
      )}
      {appState === 'dashboard' && <RecommendationDashboard />}
    </>
  );
}

export default App;
