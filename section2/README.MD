# Instructions to run

1. Ensure you are on a linux machine
2. Install Docker engine
3. Run the command in the terminal under section2 folder directory. Make sure you change the directory to the sql-scripts folder. <pre><code>docker run -d -p 5432:5432 --name my-postgres -v "path to sql-scripts folder":/docker-entrypoint-initdb.d/ postgres</code></pre>
4. postgres username: postgres. No password is set.

Done!