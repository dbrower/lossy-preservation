library(tidyverse)

file_names <- c("random_choose_output_1.csv","random_choose_output_2.csv","random_choose_output_3.csv",
                "random_choose_output_4.csv","random_choose_output_5.csv","random_choose_output_6.csv",
                "random_choose_output_7.csv","random_choose_output_8.csv","random_choose_output_9.csv",
                "random_choose_output_10.csv","random_choose_output_20.csv","random_choose_output_30.csv",
                "random_choose_output_40.csv","random_choose_output_50.csv","random_choose_output_60.csv",
                "random_choose_output_70.csv","random_choose_output_80.csv","random_choose_output_90.csv",
                "random_choose_output_100.csv")

graph_list <- list()

for (file_name in file_names) {
  # Read the CSV file
  df <- read.csv(file_name, skip = 4)
  
  df$state <- case_when(
    df$state == "M" ~ "0",
    df$state == "H" ~ "1",
    TRUE ~ as.character(df$state)
  )
  
  df <- df %>% mutate(total_hits = cumsum(state))
  df <- df %>% mutate(hit_rate = cummean(state))
  df$access_time <- ymd_hms(df$access_time)
  
  graph <- df %>%
    mutate(access_time = ymd_hms(access_time),
           year = year(access_time)) %>%
    group_by(year) %>%
    summarise(min_hit_rate = min(hit_rate)) %>%
    ggplot(aes(x = year, y = min_hit_rate)) +
    geom_point() +
    geom_smooth() +
    labs(title = file_name)  
  
  graph_list[[file_name]] <- graph
}

library(patchwork)

combined_graph <- wrap_plots(graph_list, nrow = 7, ncol = 3)

print(combined_graph)
