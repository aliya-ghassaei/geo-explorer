library(shiny)
library(shinydashboard)


# UI -----------------------------
ui <- dashboardPage(
      
## Title -------------------------
title = "Dashboard",
dashboardHeader(title = "dashboard"),

## Sidebar
dashboardSidebar(
  sidebarMenu(
    id = "nav",
    menuItem("Home", tabName = "home_tab"),
    menuItem("Map", tabName = "map_tab")
  )
),

## Body --------------------------
dashboardBody(

  tabItems(
### Home Tab -------------------------
tabItem(
  tabName="home_tab",
  fluidPage(
    fluidRow(
      h2("Home Tab Page Header"),
      br(),
      box(
        title = "Subheading",
        collapsible = T,
        collapsed = F,
        width = 12
      )
    )
  )
),

### Map Tab -------
tabItem(
  tabName = "map_tab",
  fluidPage(
    h2("Title Here"),
    leafletOutput("mapoutput", height="80vh")
    
  )
)





  )
)





)



# Server -------------------------

server <- function(input, output, session) {
  
  ## Reactive values --------
  reactive_vals <- reactiveValues()
  
  ## Home Tab
  observeEvent(
    if (input$nav == "map_tab") {
      output$map_tab_output <- "map tab output"
    }
  )
}



shinyApp(ui, server)