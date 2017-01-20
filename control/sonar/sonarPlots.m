

xlin = linspace(-10,10);
ylin = linspace(0,10);
seps = linspace(0.05,1.0);
accuracies = linspace(0.001,0.1);
speedOfSound = 1482;
sonarSepDist = 0.1;
accuracy = 0.01;

[x,y] = meshgrid(xlin,ylin);

deltaAngle = atan(y./(x-accuracy)) - atan(y./x);
deltaT = (cos(deltaAngle).* sonarSepDist) / speedOfSound;
mesh(x,y,deltaT)
hold on
xlabel('pool position(m)')
ylabel('pool position(m)')
zlabel('min time (s)')
xWorst = -0.5;
yWorst = 0.5;

deltaAngleAccurcies = atan(yWorst./(-accuracies)) - atan(yWorst/xWorst);
deltaTaccuracies = (cos(deltaAngleAccurcies).* sonarSepDist) / speedOfSound;
figure
plot(accuracies,deltaTaccuracies)
xlabel('accuracy (m)')
ylabel('min time')

deltaAngleWorst = atan(yWorst./(-accuracy)) - atan(yWorst./xWorst);
deltaTWorst = (cos(deltaAngleWorst).* seps / speedOfSound);
figure
plot(seps,deltaTWorst)
xlabel('sonar seperation (m)')
ylabel('min time (s)')

deltaTWorst = (cos(deltaAngleWorst).* sonarSepDist / speedOfSound);
%printf('min time for 1 cm accuracy with 10 cm sonar spacing: %f sec\n', deltaTWorst)

