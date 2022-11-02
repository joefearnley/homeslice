import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className="bg-gray-50">
      <Head>
        <title>Homeslice</title>
        <meta name="description" content="All of your internet locations in one place." />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="container mx-auto">
        <div className="relative min-h-screen overflow-hidden py-6 sm:py-20">
          <div className="relative px-6 pt-10 pb-8 sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
            <div className="mx-auto max-w-md">
              <div className="divide-y divide-gray-300/50">
                <div className="space-y-6 py-8 text-base leading-7 text-gray-600 text-center">
                  <h1 className="text-7xl font-bold">Homeslice</h1>
                  <h3 className="text-lg">All of your internet locations in one place.</h3>
                  <div className="sm:flex flex-row justify-evenly pt-3 w-3/4 sm:w-full">
                    <a href="/signup"  className="block sm:inline mb-7 sm:mb-0 bg-slate-800 px-6 py-2 border rounded-md text-white">Sign Up</a>
                    <a href="/login" className="block sm:inline bg-slate-400 px-6 py-2 border rounded-md text-white">Sign In</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>

      <footer className={styles.footer}>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{' '}
          <span className={styles.logo}>
            <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16} />
          </span>
        </a>
      </footer>
    </div>
  )
}
