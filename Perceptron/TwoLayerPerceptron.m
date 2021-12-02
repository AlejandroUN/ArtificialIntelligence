% XOR input
input = [0 0; 0 1; 1 0; 1 1];
%XOR
%0 0 0
%0 1 1
%1 0 1
%1 1 0
%AND
%0 0 0
%0 1 0
%1 0 0
%1 1 1
% Output que deseamos para XOR
output = [0;1;1;0];
%output = [0;0;0;1];
% Inicialización de los umbrales
bias = [-1 -1 -1];
% Coeficiente de Aprendizaje
coeff = 0.7;
% Número de iteraciones
iterations = 1000000;

%Declaración de la función sigmoidea
sigmat = '1/(1 + exp(-x))';
sigmat = strcat('@(x)', sigmat);
sigma = str2func(sigmat);

%Inicialización aleatoria de los pesos
%rand('state',sum(100*clock));
%Tendremos 9 conexiones por tanto son 9 pesos en total
weights = -1 +2.*rand(3,3);


%Creación de matriz para observar el cambio en el error conforme el avance
%de iteraciones
MSE = zeros(2,iterations)

for i = 1:iterations
   out = zeros(4,1);
   numIn = length (input(:,1));
   %Aplicamos el procedimiento para todos los "data training" que en este
   %caso son input
   for j = 1:numIn
      % 'hidden-layers'
      % Calculamos el producto punto entre los pesos y los datos
      H1 = bias(1,1)*weights(1,1) + input(j,1)*weights(1,2) + input(j,2)*weights(1,3);
      H2 = bias(1,2)*weights(2,1) + input(j,1)*weights(2,2) + input(j,2)*weights(2,3);
      % Estos resultados los ingresamos como parametro a la función
      % sigmoidea
      x2(1) = sigma(H1);      
      x2(2) = sigma(H2);

      % 'output-layer'
      x3_1 = bias(1,3)*weights(3,1) + x2(1)*weights(3,2) + x2(2)*weights(3,3);
      out(j) = sigma(x3_1);
      
      % Actualizando los delta del gradiente que son el 'steepest ascent'
      % Para el 'output-layer':
      % delta(wi) = xi*delta,
      % delta = (1-actual output)*(desired output - actual output) 
      delta3_1 = out(j)*(1-out(j))*(output(j)-out(j));
      
      % Para los 'hidden-layers'
      delta2_1 = x2(1)*(1-x2(1))*weights(3,2)*delta3_1;
      delta2_2 = x2(2)*(1-x2(2))*weights(3,3)*delta3_1;
      
      % Actualizando los pesos de las conexiones
      for k = 1:3
         if k == 1 % Los de los umbrales o 'bias'
            weights(1,k) = weights(1,k) + coeff*bias(1,1)*delta2_1;
            weights(2,k) = weights(2,k) + coeff*bias(1,2)*delta2_2;
            weights(3,k) = weights(3,k) + coeff*bias(1,3)*delta3_1;
         else % Los demás pesos
            %Los de los 'hidden-layer' 
            weights(1,k) = weights(1,k) + coeff*input(j,1)*delta2_1;
            weights(2,k) = weights(2,k) + coeff*input(j,2)*delta2_2;
            %Los del 'output-layer'
            weights(3,k) = weights(3,k) + coeff*x2(k-1)*delta3_1;
         end
      end
   end  
   %En cada iteración calculamos el error cuadrático medio
   sum = 0;
   for j = 1:numIn
    sum = (output(j)-out(j))^2;
   end
   MSE(1,i) = i;
   MSE(2,i) = sum/numIn;
end
weights
out
    %Grafica de los puntos
    title('Neurons Graphs');
    figure(1)    
    hold on
    plot(input(1,1), input(1,2),'r*');
    plot(input(2:3,1), input(2:3,2),'b*');
    plot(input(4,1), input(4,2),'r*');
    xlabel('x');
    ylabel('y');        
    
    %Gráfica de las regiones de aceptación del Perceptron MultiCapas    
    graph1t = strcat(strcat(strcat('((-(',strcat(strcat(num2str(weights(1,2),4),strcat('*x - (', num2str(weights(1,1),4))),')))/(')),num2str(weights(1,3),4)),'))');    
    graph1t = strcat('@(x)', graph1t);
    graph1t
    graph1 = str2func(graph1t);

    graph2t = strcat(strcat(strcat('((-(',strcat(strcat(num2str(weights(2,2),4),strcat('*x - (', num2str(weights(2,1),4))),')))/(')),num2str(weights(2,3),4)),'))');    
    graph2t = strcat('@(x)', graph2t);
    graph2t
    graph2 = str2func(graph2t);
    
    Xaxis = 0:7/500:1;            
    %Gráfica del error cuadrático medio 
    plot(Xaxis, graph1(Xaxis));  
    plot(Xaxis, graph2(Xaxis));  
    hold off
    
    
    figure(2)        
    title('Mean Square Error');
    hold on
    plot(MSE(1,:), MSE(2,:),'b*');    
    xlabel('iteraciones');
    ylabel('MSE');
    hold off
    