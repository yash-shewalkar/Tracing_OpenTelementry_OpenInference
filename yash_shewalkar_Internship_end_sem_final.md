<!-- Slide number: 1 -->
# End-Sem Internship Review
Presenter:  Yash Shewalkar (AI Intern at Siemens DISW)

Date: 14/05/2026

Restricted | © Siemens 2026 | Siemens Digital Industries Software | Where today meets tomorrow.

<!-- Slide number: 2 -->
# AdvantEdge AI – Siemens DISW GCO
Part of AdvantEdge AI program, an innovative AI initiative within Siemens Global Customer Operations (GCO). This program is dedicated to enhancing employee productivity, automating manual processes, and accelerating customer project timelines through the development and implementation of advanced AI tools.​

Team Composition:​
Advisors: The program is guided by experienced advisors.​
Architects: ​An experienced architect offers design insight and technical guidance, ensuring projects align with best practices and strategic goals.​
Co-ops: A dynamic team of five interns, including myself, actively contributes to various projects within the program.​

​My Role:​
As a co-op intern, I am deeply involved in several projects, collaborating closely with advisors and peers to develop innovative AI solutions. My contributions include research, development, and implementation of AI tools that align with the program's objectives.

![The image presents a stylized infinity symbol, characterized by a continuous loop with no beginning or end. The symbol is rendered in a gradient of teal hues, transitioning from a lighter shade on the right to a darker shade on the left. * **Infinity Symbol:** * The infinity symbol is a continuous loop with no beginning or end. * It is symmetrical about its vertical axis. * The symbol is depicted in a gradient of teal colors. * **Color Gradient:** * The color gradient transitions from a lighter shade of teal on the right to a darker shade on the left. * The gradient effect gives the symbol a sense of depth and dimensionality. * **Background:** * The background of the image is white. * The white background provides a clean and neutral contrast to the teal-colored infinity symbol. In summary, the image features a stylized infinity symbol with a gradient effect that adds visual interest and depth. The use of a white background helps to create a clean and simple composition. A green and blue infinity symbol AI-generated content may be incorrect.](MainshapeCombiningtherealandthedigital.jpg)
Restricted | © Siemens 2026 | Siemens Digital Industries Software | Where today meets tomorrow.

### Notes:

<!-- Slide number: 3 -->
# Mentors

Dr. Ajinkya Bhave (Director and Head, CoE India at Siemens DISW)
Omkar Mundlik (Technical Solution Architect Advantedge AI at Siemens DISW)
Sanskruti Khedkar (Technical Solution Architect Advantedge AI at Siemens DISW)
Aript Saikia (Technical Solution Architect Advantedge AI at Siemens DISW)

Restricted | © Siemens 2026 | Siemens Digital Industries Software | Where today meets tomorrow.

<!-- Slide number: 4 -->

# Internship Work
| Domain | Projects | Key Contributions | Status |
| --- | --- | --- | --- |
| RAG based AI Search service | Smart chunking strategy for complex structured JSON docs. | Indexing the data source using custom skillsets in Azure AI Search. | In Production |
| AI Agents for Simulation Workflow | Document aware agent which can provide concise response and validate the workflow models. | Building RAG documentation. Image + Text awareness Intent classification Query rewriting etc | In Development |
Page 4
Restricted | © Siemens 2023 | Siemens Digital Industries Software | Author | Department | YYYY-MM-DD

### Notes:
Scope
Automate the conversion of source data to target data.
Ensure schema matching and data integrity.
Enhance efficiency and reduce manual intervention.

<!-- Slide number: 5 -->

# RAG Based Azure AI Search Service
Project Description
Development of an AI-powered search tool to find relevant JSON chunks using hybrid (keyword + semantic) search technique.
Addressed challenge:
Providing a Reliable Search service for RAG based tool calling agent which provides accurate results.

 My role and Contributions:
Research and development of POC
Iterative Testing with QA engineer.

Architecture
Outcome
Time Saved: Search service was able to filter out chunks based on the subdomain user wants to search in.

![The image presents a comprehensive flowchart illustrating the process of data ingestion, processing, and query flow for an AI-powered search system. The chart is divided into four main sections: Data Ingestion, AI Processing, Response Generation, and RAG Query Flow. **Data Ingestion** * JSON Documents * Azure Blob Storage * Azure AI Search Data Source * Indexer **AI Processing** * Skillset Processing * Document Chunking * Embedding Generation * Azure AI Search Index **Response Generation** * Top Relevant Chunks * Grounded Response **RAG Query Flow** * User Query * AI Agent * Azure AI Search Service The flowchart provides a clear and concise overview of the steps involved in ingesting data, processing it using AI, generating responses, and handling user queries. The use of arrows and boxes effectively illustrates the flow of data and the relationships between different components of the system. Overall, the image presents a well-organized and easy-to-follow visual representation of the AI-powered search system's architecture.](Picture15.jpg)
Scope
Designed and implemented a RAG-compatible enterprise search layer using Azure AI Search.
Implemented semantic + keyword hybrid search for improved retrieval accuracy.
Developed custom skillset pipeline to process and chunk structured JSON documents.
Integrated the search service with an AI Agent for tool-based retrieval and response generation

Solution
Developed Azure AI Search Skillset which a two main submodels in the hierarchy.
Used the chunking separately on both and isolated the chunks in two categories.
Restricted | © Siemens 2026 | Siemens Digital Industries Software
Page 5

<!-- Slide number: 6 -->

# Sample JSON:

![The image displays a JSON (JavaScript Object Notation) object, which is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. The JSON object in the image appears to represent the output of a workflow or a task execution, likely in a cloud-based or distributed computing environment. Here is a breakdown of the JSON object: * **workflowId**: A unique identifier for the workflow, which is "WF-2026-991". * **Input**: This section contains the input parameters for the workflow or task. * **requestMetadata**: Metadata about the request, including the source ("enterprise-portal"), priority ("high"), and potentially other fields that are omitted for brevity. * **payload**: The main payload of the request, which includes: * **documents**: A list of documents, with at least one document identified by "DOC-1001". Each document has a "content" field that contains sections, and a "processingConfig" field that specifies the configuration for processing, including the provider ("Azure OpenAI"), model ("gpt-4o"), and evaluation framework. * **Output**: This section contains the output of the workflow or task. * **status**: The status of the workflow or task, which is "completed". * **generatedArtifacts**: A list of generated artifacts, including a JSON output with entities, such as "CustomerAccount". * **evaluationResults**: The results of the evaluation, including an overall score of 0.91 and detailed metrics such as faithfulness (0.93) and context precision. * **executionMetadata**: Metadata about the execution, including the duration in milliseconds (18220). The JSON object provides a structured way to represent the input, output, and metadata of a workflow or task execution, making it easier to parse, generate, and exchange data between systems. The use of JSON objects like this is common in cloud-based services, APIs, and data exchange protocols, where structured data needs to be transmitted and processed efficiently. In terms of applications, this JSON object could be used in various scenarios, such as: * **Document processing and analysis**: The JSON object could represent the input and output of a document processing pipeline, where documents are analyzed and evaluated using AI models like Azure OpenAI. * **Workflow management**: The JSON object could be used to represent the state of a workflow or task execution, including input parameters, output results, and metadata. * **Data exchange and integration**: The JSON object could be used as a data exchange format between different systems, services, or APIs, allowing them to communicate and integrate with each other. Overall, the JSON object in the image provides a concise and structured way to represent complex data, making it easier to work with and exchange data between systems.](Picture7.jpg)

Page 6
Restricted | © Siemens 2022 | Siemens Digital Industries Software | Author | Department | YYYY-MM-DD

<!-- Slide number: 7 -->

Document Aware Agent
AI Agents for Simulation Workflow
Benefits

Faster and easier access to precise, documented content.

Answers based on exact slides and sections relevant to the user’s question.

Provides relevant images gathered from the documentation in the answer.

Early Model Validation through automated, documentation-based cross-checking.

Deeper Knowledge base
Instant Answers
Assistant can understand both text and images in the document PPTs.
This ensures high relevancy in answers.
Get grounded answers to any question related to the workflow documentations in a concise format.

Features

Under
Development

Model Validation
Guidance
Agent can assess your model using MCP server.
It can validate it with best practices from the documentation.
Ask any question and get step-by-step guidance for building any workflow.

- UC735

<!-- Slide number: 8 -->

Amesim Model.py / .ame
# Sample Amesim Model:

![The image displays a computer code written in Python, which appears to be used for creating and configuring a simulation model using the Amesim API. The code imports necessary modules, initializes the Amesim Python API, creates a new system, adds components, sets parameters, and establishes connections. * **Importing Modules and Initializing Amesim API** * The code starts by importing the necessary modules, including `os` and `sys`. * It checks if the `ame_apy` module is already loaded and attempts to import it if not. * If the import fails, it prints an error message indicating that the Simcenter Amesim API module could not be imported. * The Amesim Python API is initialized using `AMEInitAPI()`. * **Creating a New System and Adding Components** * A new system called "MyModel_py" is created using `AMECreateCircuit('MyModel_py')`. * A component called "mass_friction1port" is added to the system with coordinates (10, 99) using `AMEAddComponent()`. * The submodel of the "mass_friction1port" component is set to "MAS003" using `AMEChangeSubmodel()`. * **Setting Parameters** * Various parameters of the "mass_friction1port" component are set using `AMESetParameterValue()`, including: * `v1` * `x1` * `actRfrict` * `energyRfrict` * `actIMass` * `energyIMass` * `actSGrav` * `energySGrav` * `mass` * `coefv` * `wind` * `coul` * `stict` * `angle` * **Establishing Connections** * The code mentions establishing connections inside the 'top circuit' but does not provide specific details on how these connections are made. In summary, this code is used to create and configure a simulation model using the Amesim API, specifically adding a "mass_friction1port" component to a new system, setting its parameters, and preparing for establishing connections within the system.](Picture9.jpg)
Amesim Model

![The image presents a comprehensive diagram of an electric vehicle's powertrain system, showcasing the intricate relationships between various components. The diagram is divided into distinct sections, each representing a crucial aspect of the vehicle's operation. **Main Components:** * **Battery:** Represented by a green rectangle with a plus sign and a minus sign, the battery is the primary energy source for the vehicle. * **Electric Motor:** Symbolized by a green circle with the letter "M" inside, the electric motor converts electrical energy from the battery into mechanical energy to propel the vehicle. * **Vehicle Control Unit (VCU):** Depicted as a green rectangle with the label "VCU ELEC," the VCU is the brain of the vehicle, responsible for controlling and coordinating the various systems. * **Driver:** Represented by a green rectangle containing a person icon, the driver interacts with the vehicle through various inputs, such as acceleration and braking. * **Vehicle:** Illustrated as a green car icon, the vehicle is the end product of the powertrain system, with the system's ultimate goal being to propel it efficiently. **Connections and Flow:** * **Red Lines:** Indicate the flow of electrical energy between components, highlighting the connections between the battery, electric motor, and VCU. * **Green Lines:** Represent the mechanical connections between components, such as the electric motor, reduction ratio, and vehicle. * **Purple Lines:** Signify the communication and control signals exchanged between the VCU, driver, and other components. **Key Interactions:** * **Driver Input:** The driver's inputs, such as acceleration and braking, are transmitted to the VCU, which then adjusts the electric motor's output accordingly. * **VCU Control:** The VCU receives data from various sensors and sends control signals to the electric motor, regulating its speed and torque. * **Energy Flow:** The battery supplies electrical energy to the electric motor, which converts it into mechanical energy to propel the vehicle. **Additional Elements:** * **Reduction Ratio:** A gear system that adjusts the torque and speed of the electric motor's output to optimize efficiency and performance. * **Sensors and Feedback:** Various sensors, represented by icons such as a speedometer and an accelerometer, provide feedback to the VCU, enabling it to make adjustments and optimize the vehicle's performance. In summary, the diagram provides a detailed illustration of an electric vehicle's powertrain system, highlighting the complex interactions between the battery, electric motor, VCU, driver, and vehicle. The use of different colored lines and icons effectively conveys the flow of energy, control signals, and mechanical connections between components, offering a comprehensive understanding of the system's operation.](Picture4.jpg)

Page 8
Restricted | © Siemens 2022 | Siemens Digital Industries Software | Author | Department | YYYY-MM-DD

<!-- Slide number: 9 -->

AI Agents for Simulation Workflow
 My role and Contributions:
Research and development of POC
Production deployment on Azure.
                              Solution
Create Custom Skillset which can analyze image and create its description as text to build a RAG over it.

For Real-time access of Model Status in Amesim create a MCP server which will directly send logs of Amesim software through a backend server to which MCP can communicate.

Integrate the Azure AI Search service as a tool for Agent.

Create Workflow Agent to handle documentation related task and workflow steps related task.

Create Amesim Agent to handle Model Inspection related task.

Create a Supervisor Agent which can route the task to specific agent based on user query.
Architecture

![The image presents a comprehensive flowchart illustrating the architecture of an AI system, comprising various components and their interactions. The chart is divided into several sections, each representing a distinct aspect of the system. **Simulation Software** * **AMESim** * Realtime Logs * Custom Backend Server * MCP Tool Server Backend Log Service **MCP Server** * Latest Model Config Logs **Model Validation Logic** * **Agent Model Understanding** * Documentation Verification using RAG * Validation Comments / Suggestions **Central AI Agent** * **Supervisor Agent** * Routes user queries based on the task to specialized agents * **Specialized Agents** * **Workflow Agent** * Handles documentations (RAG) related tasks, workflow steps related tasks * **AMESim Agent** * Handles AMESim model inspection related tasks **Query Processing** * **Query Rewrite Needed?** * No * Yes → Rewritten Query * **Azure AI Search Service** * **RAG Retrieval Layer** * Vector + Keyword Index The flowchart illustrates the following key points: * The system begins with simulation software, which includes AMESim, real-time logs, custom backend server, and MCP tool server backend log service. * The MCP server receives the latest model config logs and interacts with the central AI agent. * The central AI agent consists of a supervisor agent that routes user queries to specialized agents, including workflow agents and AMESim agents. * The system features a query processing component that determines whether a query rewrite is needed, and if so, it proceeds to rewrite the query. * The Azure AI search service and RAG retrieval layer are also integral parts of the system, utilizing vector and keyword indexes. In summary, the image provides a detailed overview of the AI system's architecture, highlighting its various components, their interactions, and the flow of data between them.](Picture4.jpg)
Restricted | © Siemens 2026 | Siemens Digital Industries Software
Page 9

<!-- Slide number: 10 -->

# RAG Quality Evaluation:  RAGAS Metrics

![The image presents a flowchart illustrating the process of evaluating the performance of a retrieval-based question answering system. The chart is divided into two main sections: "Retrieval Evaluation Metrics" and "Response Evaluation Metrics." **Main Points:** * **User Input/Query** + Retrieves information from a retriever * **Retriever** + Retrieves context * **Retrieved Context** + Evaluation metrics: - Context Relevancy - Context Precision - Context Recall - Noise Sensitivity * **Ground Truth Answer** + Used for evaluation * **LLM Generation** + Generates response * **Generated Response** + Evaluation metrics: - Response Evaluation Metrics - Answer Relevancy - Answer Correctness - Answer Similarity - Faithfulness **Summary:** The flowchart outlines the steps involved in evaluating the performance of a retrieval-based question answering system. The process begins with user input or query, which is then retrieved by the retriever. The retrieved context is evaluated using various metrics, including context relevancy, precision, recall, and noise sensitivity. The ground truth answer is used for evaluation, and the LLM generation produces a response. The generated response is then evaluated using response evaluation metrics, including answer relevancy, correctness, similarity, and faithfulness. Overall, the flowchart provides a clear and concise overview of the evaluation process for retrieval-based question answering systems.](Picture4.jpg)
Page 10
Restricted | © Siemens 2022 | Siemens Digital Industries Software | Author | Department | YYYY-MM-DD

<!-- Slide number: 11 -->

# Tracing : Opentelementry in VS code and AI Toolkit

![The image presents a screenshot of a computer screen displaying a list of chat completions, with the following details: * **Chat Completion** * trace_01J2...6X8 * What are the key benefits of... * 2.35s * Success * 11:24:51 AM * **Azure OpenAI GPT-4o** * What are the key benefits of... * 2.18s * Success * 11:24:51 AM * **Embedding - ada-002** * key benefits, advantages, pr * 320ms * Success * 11:24:50 AM * **Vector DB - query** * similarity_search * 480ms * Success * 11:24:50 AM * **Data Source - documents** * faq_benefits.pdf (3 chunks) * 150ms * Success * 11:24:50 AM * **ChatCompletion** * trace_01J2...6X9 * How does RAG improve AI mo.. * 3.12s * Success * 11:24:10 AM * **ChatCompletion** * trace_01J2...7A0 * Summarize this document * 1.85s * Success * 11:23:58 AM * **ChatCompletion** * trace_01J2...7A1 * What is the pricing for Azure... * 2.01s * Error * 11:23:41 AM * **ChatCompletion** * trace_01J2...7A2 * Compare GPT-4o and GPT-4 * 2.67s * Success * 11:23:15 AM The image displays a list of chat completions, each with a unique trace ID, input text, latency, status, and timestamp. The list includes various chat completions, including ones related to Azure OpenAI GPT-4o, embeddings, vector DB queries, and data sources. The latency times range from 150ms to 3.12s, and the status is mostly "Success," except for one entry with an "Error" status. The timestamps indicate that the chat completions occurred at different times, with the most recent one happening at 11:24:51 AM. Overall, the image provides a snapshot of a chat completion system's activity, showcasing its performance and any potential issues.](Picture6.jpg)
Page 11
Restricted | © Siemens 2022 | Siemens Digital Industries Software | Author | Department | YYYY-MM-DD

<!-- Slide number: 12 -->

# Chatbot UI in React  using Siemens IX Component Library

![The image presents a comprehensive overview of the components used in a design system, showcasing their organization into intuitive categories. The title "Components Overview" is prominently displayed at the top, followed by a brief description that highlights the purpose of the design system. * **Application frame**: - A rectangular box representing the main application window. * **Navigation and hierarchy**: - A horizontal line with multiple sections, indicating a menu or breadcrumb trail. * **Containers and layouts**: - A box with a smaller box inside it, symbolizing a container or layout component. * **Forms**: - A rectangular box with several lines and fields, representing a form. * **Input fields and selections**: - A circle with three horizontal lines and a rectangular box with a line through it, indicating input fields and selection options. * **Buttons and actions**: - Two rectangular boxes with rounded corners, representing buttons. * **System feedback and status**: - A rectangular box with a progress bar and a circle with a line through it, indicating system feedback and status updates. * **Data display**: - A table with rows and columns, representing data display. * **Charts**: - A bar graph, symbolizing chart components. The image effectively communicates the various components available in the design system, making it easy for users to find the right tools for their app design projects.](Picture6.jpg)
Page 12
Restricted | © Siemens 2022 | Siemens Digital Industries Software | Author | Department | YYYY-MM-DD

<!-- Slide number: 13 -->

# Tech Stack
Programming languages and Frameworks:

![The image presents a stylized, pixelated representation of the Python logo, rendered in a metallic silver color with a carbon fiber pattern. The logo is set against a solid black background. * The logo features a distinctive design with two interconnected loops. * The loops are curved and smooth, forming a continuous shape. * The top loop has a small circle at its upper left corner, while the bottom loop has a similar circle at its lower right corner. * The loops are connected by a curved line that forms the body of the Python logo. * The logo's surface exhibits a metallic silver color with a carbon fiber pattern. * The carbon fiber pattern is visible throughout the logo, giving it a textured appearance. * The metallic silver color provides a sleek and modern look to the logo. * The background of the image is a solid black color. * The black background helps to accentuate the logo's metallic silver color and carbon fiber pattern. In summary, the image showcases a unique and visually appealing representation of the Python logo, characterized by its metallic silver color, carbon fiber pattern, and stylized design. The solid black background effectively highlights the logo's features, making it stand out. Download Python Logo PNG Vector - GSS TECHNOLOGY](Picture21.jpg)

![The image presents a simple yet distinctive design, featuring the word "Streamlit" in large gray text against a black background. The logo is centered and symmetrical, with the word positioned below a crown-like symbol. * **Crown-like Symbol** + Located at the top center of the image + Dark gray color + Resembles a crown or a boat + Composed of three triangular shapes * **Streamlit Text** + Positioned below the crown-like symbol + Large gray font + Centered horizontally + Reads "Streamlit" In summary, the image features a clean and minimalist design, with a prominent display of the Streamlit logo and text on a solid black background. The use of a crown-like symbol adds a touch of elegance and sophistication, while the large gray text ensures clear visibility and readability. Overall, the image effectively communicates the Streamlit brand identity in a simple yet effective manner. Brand • Streamlit](Picture23.jpg)

![The image presents a striking black-and-white illustration of a flask, accompanied by the word "Flask" in bold, serif font. The flask is depicted in a dynamic pose, with its spout pointing to the right and its handle extending upwards towards the top-left corner of the image. The flask's body features a curved shape, reminiscent of a horn or a tusk, with a textured appearance that suggests a rugged, organic material. A small loop adorns the top of the flask, likely serving as a handle or attachment point. The spout is short and stubby, while the handle is long and curved, evoking the shape of a horn. Below the flask, the word "Flask" is emblazoned in large, bold letters, with each letter featuring a distinctive serif design. The text is centered and spans the width of the image, drawing attention to the object above. The background of the image is a clean and crisp white, providing a stark contrast to the detailed, high-contrast illustration of the flask. Overall, the image effectively showcases the flask's unique design and features, making it a compelling visual representation. Flask Logo PNG Transparent & SVG Vector - Freebie Supply](Picture22.jpg)
Deployment:

![The image features the React logo, a stylized atom symbol with the word "React" written below it. * The logo is centered in the image and consists of: + A white atom symbol with six curved lines extending from a central circle. + The atom symbol is symmetrical, with three curved lines on each side of the center circle. * Below the logo, the word "React" is written in: + Large, bold, white text. + A simple sans-serif font. The background of the image is solid black, providing a clean and simple contrast to the white logo and text. Overall, the image effectively communicates the brand identity of React, a popular JavaScript library for building user interfaces. React original wordmark logo - free Icon PNG, SVG](Picture8.jpg)

![The image presents a logo for Azure Functions, a cloud-based serverless compute service. The logo features a stylized lightning bolt and angular brackets, accompanied by the text "Azure Functions" in blue. * **Logo:** * The logo is positioned on the left side of the image. * It consists of a yellow lightning bolt with a pointed tip, situated within a pair of blue angular brackets. * The lightning bolt is oriented vertically, with its top end pointing towards the upper-left corner of the image. * The angular brackets are symmetrical, with their open ends facing outward. * **Text:** * The text "Azure Functions" is displayed in blue font to the right of the logo. * The text is written in a sans-serif font and is centered horizontally. * **Background:** * The background of the image is white. In summary, the image effectively represents the Azure Functions brand with its distinctive logo and clear typography, set against a clean white background.](Picture7.jpg)

![The image features a logo and text on a black background. * The logo is positioned at the top center of the image. * It consists of a purple container icon encircled by a teal line, accompanied by two teal dots. * The container icon is composed of three rectangular shapes of varying sizes, stacked on top of each other. * Below the logo, there is white text that reads "Azure Container Apps". * The text is written in a simple sans-serif font. * The text is centered and takes up about one-third of the image's width. The image appears to be a logo or header for Azure Container Apps, likely used as a visual identifier for the service.](Picture14.jpg)

![The image presents a logo for "ragas," featuring a distinctive design that incorporates a triangle and a ruler. * The logo consists of two main elements: + A yellow triangle with a ruler on its side + The word "ragas" in white text * The triangle is positioned to the left of the text, with its base facing upwards. + The triangle features a ruler along its hypotenuse, marked with measurements in centimeters. + The triangle's color is a vibrant yellow, while the ruler markings are black. * The text "ragas" is displayed in large, white letters to the right of the triangle. + The font used for the text is clean and sans-serif. + The text is centered vertically within the image. The logo effectively combines a geometric shape with a common tool used for measurement, potentially symbolizing precision or construction. The use of a yellow triangle and white text against a black background creates a visually striking contrast. Overall, the design appears modern and professional, suggesting that it may be used as a logo for a company or brand in the fields of architecture, engineering, or design.](Picture19.jpg)

Databases:

![The image depicts a blue hexagon with a white outline of a document in the center. The document outline contains the numbers "10" and "01" in white text. * **Blue Hexagon:** * Shape: Hexagon * Color: Blue * **White Document Outline:** * Shape: Rectangular with a folded corner * Color: White * **Numbers:** * Number 1: 10 * Number 2: 01 * Color: White The image appears to be a logo or icon, possibly representing a binary code or data storage concept. A blue hexagon with black text and numbers AI-generated content may be incorrect.](Picture5.jpg)
Azure Blob Storage
Cloud service:

![The image presents a logo for OpenAI, a prominent artificial intelligence research organization. The logo features a stylized design that incorporates the company's name and initials. * **Logo Design** * The logo consists of two parts: a stylized letter "A" and a circular symbol. * The letter "A" is depicted in blue and white, with a 3D effect that gives it a sense of depth. * The circular symbol is black and white, featuring a knot-like design that represents the interconnectedness of AI systems. * **OpenAI Text** * To the right of the logo, the text "OpenAI" is displayed in large, bold font. * The text is written in black, providing a clear and readable contrast to the white background. * **Background** * The background of the image is plain white, which helps to focus attention on the logo and text. In summary, the image effectively communicates the OpenAI brand identity through its distinctive logo and clear typography. The use of a stylized design and bold font creates a professional and modern visual representation of the organization. Azure Open AI | Transforming AI Development for Businesses](Picture33.jpg)

![The image presents a visually striking graphic that combines a cloud icon with a magnifying glass and the text "AI Search" against a black background. * **Cloud Icon:** * The cloud icon is centered in the image, featuring a white outline that provides a clear definition. * The cloud itself is depicted in a gradient of gray lines, transitioning from light to dark, which gives it a sense of depth and dimensionality. * A magnifying glass icon is superimposed over the cloud, adding a layer of complexity to the design. * **Magnifying Glass Icon:** * The magnifying glass icon is positioned within the cloud, with its handle pointing towards the bottom-left corner. * The magnifying glass features a thick line for its body and a thin line for its outline, creating visual contrast. * **Text:** * Below the cloud icon, the text "AI Search" is displayed in a thin white font, which provides a clear and legible contrast to the dark background. * The text is centered and written in all capital letters, emphasizing its importance. * **Background:** * The background of the image is a solid black color, which helps the cloud and magnifying glass icons stand out. * A white border on either side of the image adds a touch of elegance and frames the content. In summary, the image effectively combines a cloud icon with a magnifying glass and the text "AI Search" to create a visually appealing graphic. The use of contrasting colors and clear typography makes the image easy to understand and interpret. Azure Cloud Services | Sysvine Technologies](Picture4.jpg)

![The image depicts a logo for Azure Cosmos DB, a globally distributed database service offered by Microsoft Azure. * The logo features a stylized illustration of the Earth: + The Earth is depicted in a simple, flat style, with a blue ring around it. + The planet is colored green and blue, representing landmasses and oceans. * A blue ring surrounds the Earth: + The ring is curved and open, suggesting movement or orbit. + It may represent the global distribution and connectivity of Azure Cosmos DB. * Three blue shapes are placed around the Earth: + A four-pointed star shape is located in the top-left corner. + A circle is positioned in the top-right corner. + A smaller circle is situated below the larger one on the right side. * Text is displayed below the Earth: + The text reads "Azure Cosmos DB" in a simple, black font. The logo effectively conveys the global and distributed nature of Azure Cosmos DB through its use of a stylized Earth and orbiting ring, accompanied by simple yet distinctive shapes.](Picture17.jpg)
Page 13
Restricted | © Siemens 2022 | Siemens Digital Industries Software | Author | Department | YYYY-MM-DD

<!-- Slide number: 14 -->
# Thank You!
Page 14
Restricted | © Siemens 2022 | Siemens Digital Industries Software | Author | Department | YYYY-MM-DD