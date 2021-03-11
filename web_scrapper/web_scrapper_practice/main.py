from indeed_js import indeed_js_jobs
from so_js import so_js_jobs
from save_to_file import save_to_file

indeed_js_jobs = indeed_js_jobs()
so_js_jobs = so_js_jobs()

job_list = indeed_js_jobs + so_js_jobs

save_to_file(job_list)
